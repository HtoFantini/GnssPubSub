from gpspublisher.devices.gps_devices import Neo6M

device = Neo6M()

dic = device.read_raw_data()

filt_dic = device.filtered_gps_data()
