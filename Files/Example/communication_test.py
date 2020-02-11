"""//////////////////////////////////////////////////////////////////////////////
//                                                                             //
//    Copyright © 2017  Daniel Gutierrez-Galan                                 //                           //
//                                                                             //
//    You should have received a copy of the GNU General Public License        //
//    along with NAVIS Tool.  If not, see<http://www.gnu.org/licenses/> .      //
//                                                                             //
//////////////////////////////////////////////////////////////////////////////"""

#--- Importing  libraries ---#
import spynnaker8 as p
import pylab
import numpy as np
import matplotlib.pyplot as plt
import pyNN.utility.plotting as plot


#--- simulation setup ---#
p.setup(timestep=1.0, min_delay=1.0, max_delay=144.0)


#-- Config parameters --#
t = 200                    #time of simulation in ms


#--- Neuron type parameters ---#
cell_params_lif = {'cm': 0.25,
                   'i_offset': 0.0,
                   'tau_m': 20.0,
                   'tau_refrac': 2.0,
                   'tau_syn_E': 5.0,
                   'tau_syn_I': 5.0,
                   'v_reset': -68.0,
                   'v_rest': -65.0,
                   'v_thresh': -50.0
                   }

def create_projections(n, w, d):
    projections = list()
    for i in range(n):
        singleConnection = ((i, i, w, d))
        projections.append(singleConnection)
    return projections


cochlea_pop = p.Population(size=64, cellclass=p.external_devices.ExternalCochleaDevice(spinnaker_link_id=0, board_address=None, cochlea_key=0x200, cochlea_n_channels=p.external_devices.ExternalCochleaDevice.CHANNELS_64, cochlea_type=p.external_devices.ExternalCochleaDevice.TYPE_MONO, cochlea_polarity=p.external_devices.ExternalCochleaDevice.POLARITY_MERGED), label="ExternalCochlea")

middle_pop = p.Population(4, p.IF_curr_exp, cell_params_lif, label='middle_pop')

out_pop = p.Population(4, p.IF_curr_exp, cell_params_lif, label='out_layer')

#p.Projection(cochlea_pop, out_pop, p.FromListConnector(create_projections(4, 1.2, 1.0)))

p.Projection(cochlea_pop, middle_pop, p.OneToOneConnector(), synapse_type=p.StaticSynapse(weight=1.2, delay=1.0))

p.Projection(middle_pop, out_pop, p.OneToOneConnector(), synapse_type=p.StaticSynapse(weight=1.2, delay=1.0))

out_pop.record(["spikes", "v"])

p.external_devices.activate_live_output_to(out_pop, cochlea_pop)

#---runing simulation ---#
p.run(t)

neo =out_pop.get_data(variables=["spikes", "v"])
spikes = neo.segments[0].spiketrains
print spikes
v = neo.segments[0].filter(name='v')[0]
print v

#--- Finish simulation ---#
p.end()

#--- Variables for saving spikes ---#




plot.Figure(
    # plot voltage for first ([0]) neuron
    plot.Panel(v, ylabel="Membrane potential (mV)",
               data_labels=[out_pop.label], yticks=True, xlim=(0, t)),
    # plot spikes (or in this case spike)
    plot.Panel(spikes, yticks=True, markersize=5, xlim=(0, t)),

    title="Simple Example",
    annotations="Simulated with {}".format(p.name())
)
plt.show()
