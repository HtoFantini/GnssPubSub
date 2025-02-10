import serial

from gpspublisher.utils.constants import DICT_DEFAULT_PORTS


def read_raw_serial(serial_port=None, baudrate=9600) -> str:
    """_summary_

    Args:
        serial_port (_type_, optional): _description_. Defaults to None.
        baudrate (int, optional): _description_. Defaults to 9600.

    Returns:
        str: _description_
    """

    if serial_port is None:
        serial_port = DICT_DEFAULT_PORTS['Serial']

    # TODO Uncomment serial read an comment constant lines

    # with serial.Serial(serial_port, baudrate, timeout=1,
    #                    bytesize=serial.EIGHTBITS,
    #                    parity=serial.PARITY_NONE,
    #                    stopbits=serial.STOPBITS_ONE) as serial_port:

    #     lines = serial_port.read(size=int(10e5)) \
    #         .decode('utf-8', errors='replace') \
    #         .strip()

    lines = ("$GPVTG,140.88,T,,M,8.04,N,14.89,K,D*05\r\n"
             "$GPGGA,184353.07,1929.045,S,02410.506,"
             "E,1,04,2.6,100.00,M,-33.9,M,,0000*6D\r\n"
             "$GPRMC,123519,A,4807.038,N,01131.000,E"
             ",022.4,084.4,230394,003.1,W*6A")

    return lines
