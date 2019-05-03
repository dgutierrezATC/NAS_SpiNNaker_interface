# Interfacing the Neuromorphic Auditory Sensor with the SpiNNaker board

1. Go to "Files" folder.
2. Go to "Python" folder.
3. Go to "spinnaker" folder.
4. Copy the file "external_spinnaker_link_cochlea_device.py" in "...\Anaconda2\Lib\site-packages\spynnaker\pyNN\external_devices_models".
5. Go back to "Python" folder.
6. Go to "spinnaker8" folder.
7. Copy the file "external_spinnaker_link_cochlea_device.py" in "...\Anaconda2\Lib\site-packages\spynnaker8\external_device_models".

# How to use the NAS external device class:

1. In your Python code, copy the following line:

cochlea_pop = p.Population(size=64, cellclass=p.external_devices.ExternalCochleaDevice(spinnaker_link_id=1, board_address=None, cochlea_key=0x200, cochlea_n_channels=p.external_devices.ExternalCochleaDevice.CHANNELS_64, cochlea_type=p.external_devices.ExternalCochleaDevice.TYPE_MONO, cochlea_polarity=p.external_devices.ExternalCochleaDevice.POLARITY_MERGED), label="ExternalCochlea")
