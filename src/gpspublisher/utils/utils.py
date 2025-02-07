from functools import wraps
import serial
import pynmea2
import time
from typing import Dict
from typing import List

from gpspublisher.utils.constants import DICT_NMEA, SOG_CONST, DICT_DEFAULT_PORTS


def str_datetime_formated() -> str:
    """_summary_

    Returns:
        str: _description_
    """
    datet = (time.strftime("%a %d %b %H:%M:%S %z", time.localtime())[:-2]
             + time.strftime(" %Y", time.localtime()))
    return datet


def extract_keys() -> List[str]:
    """Extract all GPS dataframe columns

    Returns:
        List[str]: _description_
    """
    li_out = []
    for dic_gp in DICT_NMEA:
        for li_fields in dic_gp.values():
            for dic_field in li_fields:
                for dic_name in dic_field.values():
                    name = dic_name['name']
                    if name not in li_out:
                        li_out.append(name)
    return li_out


def errors_pynmea(func):
    """Exception pynmea

    Args:
        func (_type_): _description_

    Returns:
        _type_: _description_
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except pynmea2.ParseError:
            # print(f"{func.__name__}: Parse error: {e}")
            result = {}
        return result
    return wrapper


@errors_pynmea
def _get_fields_pynmea_parse(line_gps: str, type_line: str = None) -> Dict:
    msg = pynmea2.parse(line_gps)
    dicio = {}

    type_line = msg.sentence_type
    li_full_data = next(
        ele[type_line] for ele in DICT_NMEA
        if next(iter(ele.keys())) == type_line
    )

    for field in li_full_data:
        nome = next(iter(field))
        nome_dic = field[nome]['name']
        value = getattr(msg, nome) if hasattr(msg, nome) else ""

        if value != "":
            dicio[nome_dic] = value

        if nome.endswith('_grnd'):
            dicio[nome_dic] = (
                float(dicio[nome_dic])*SOG_CONST
                if isinstance(dicio[nome_dic], float)
                else dicio[nome_dic]
            )

        if nome == 'datestamp':
            dicio[nome_dic] = str(dicio[nome_dic])

    return dicio


def get_gps_nmea_info_serial(protocol, baudrate, serial_port=None):

    if serial_port is None:
        serial_port = DICT_DEFAULT_PORTS['Serial']

    def get_gps_dict(serial_port=None):

        lines = serial_port.read(size=int(10e5)) \
            .decode('utf-8', errors='replace') \
            .strip()

        # TODO until here: read_raw() -> str

        # TODO from here: filter_raw(str) -> dict
        gps_info = dict(zip(extract_keys(), ""))
        li_keys_nmea = [list(ele.keys())[0] for ele in protocol]

        # lines = ("$GPVTG,140.88,T,,M,8.04,N,14.89,K,D*05\r\n"
        #         "$GPGGA,184353.07,1929.045,S,02410.506,"
        #         "E,1,04,2.6,100.00,M,-33.9,M,,0000*6D\r\n"
        #         "$GPRMC,123519,A,4807.038,N,01131.000,E"
        #         ",022.4,084.4,230394,003.1,W*6A")

        for line_ in lines.split('\r\n'):
            if any(cod in line_ for cod in li_keys_nmea):
                dicio_upd = _get_fields_pynmea_parse(line_)
                gps_info = {**gps_info, **dicio_upd}

                if 'error' in dicio_upd:
                    datef = str_datetime_formated()
                    print(f'{datef}: gps_info: error in dicio_upd '
                          f'{dicio_upd["error"]}')
        # TODO until here: filter_raw(str) -> dict
        return gps_info

    with serial.Serial(serial_port, baudrate, timeout=1,
                       bytesize=serial.EIGHTBITS,
                       parity=serial.PARITY_NONE,
                       stopbits=serial.STOPBITS_ONE) as serial_port:
        # TODO read_raw: no need get_gps_dict funtion
        return get_gps_dict(serial_port)
