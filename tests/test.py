from gpspublisher.devices.gps_devices import Neo6M

device = Neo6M()

dic = device.read_raw_data()

filt_dic = device.filtered_gps_data()


# TODO create systemic test READ_RAW (mock serial.read) -> string

# TODO create systemic test FILTER_RAW (mock serial.read) -> dict

# TODO create systemic test FORMAT_RAW (mock serial.read) -> formato dict
