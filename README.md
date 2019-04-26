# Interfacing the Neuromorphic Auditory Sensor with the SpiNNaker board

How to use it:

cochlea_pop = p.Population(size=64, cellclass=p.external_devices.ExternalCochleaDevice(spinnaker_link_id=1, board_address=None, cochlea_key=0x200, cochlea_n_channels=p.external_devices.ExternalCochleaDevice.CHANNELS_64, cochlea_type=p.external_devices.ExternalCochleaDevice.TYPE_MONO, cochlea_polarity=p.external_devices.ExternalCochleaDevice.POLARITY_MERGED), label="ExternalCochlea")
