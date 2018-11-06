"""//////////////////////////////////////////////////////////////////////////////
//                                                                             //
//    Adapted by Daniel Gutierrez-Galan			                               //
//                                                                             //
//    This file belongs to the SpiNNaker project, from the University .		   //
//    of Manchester.                                                           //
//    The code has been adapted from the original version to support           //
//    the communication between the Neuromorphic Auditory Sensor (NAS)         //
//    and the SpiNNaker board through the SpiNN-link.                          //
//         																	   //
//////////////////////////////////////////////////////////////////////////////"""

from spynnaker8.utilities import DataHolder
from spynnaker.pyNN.external_devices_models import ExternalCochleaDevice


class ExternalCochleaDeviceDataHolder(DataHolder):

	CHANNELS_256 = ExternalCochleaDevice.CHANNELS_256
	CHANNELS_128 = ExternalCochleaDevice.CHANNELS_128
	CHANNELS_64 = ExternalCochleaDevice.CHANNELS_64
	CHANNELS_32 = ExternalCochleaDevice.CHANNELS_32
	CHANNELS_16 = ExternalCochleaDevice.CHANNELS_16
	TYPE_MONO = ExternalCochleaDevice.TYPE_MONO
	TYPE_STEREO = ExternalCochleaDevice.TYPE_STEREO
	POLARITY_UP = ExternalCochleaDevice.POLARITY_UP
	POLARITY_DOWN = ExternalCochleaDevice.POLARITY_DOWN
	POLARITY_MERGED = ExternalCochleaDevice.POLARITY_MERGED

	def __init__(
            self, cochlea_n_channels, cochlea_key, spinnaker_link_id, cochlea_type, cochlea_polarity,
            label=ExternalCochleaDevice.default_parameters['label'],
            board_address=ExternalCochleaDevice.default_parameters[
                'board_address']):
		DataHolder.__init__(
			self, {'spinnaker_link_id': spinnaker_link_id, 'cochlea_n_channels': cochlea_n_channels,
					'board_address': board_address, 'label': label,
					'cochlea_key': cochlea_key, 'cochlea_type': cochlea_type, 'cochlea_polarity': cochlea_polarity})

	@staticmethod
	def build_model():
		return ExternalCochleaDevice

	def get_n_neurons(self):
		return ExternalCochleaDevice.get_n_neurons(
            self._data_items['cochlea_n_channels'], self._data_items['cochlea_type'])
