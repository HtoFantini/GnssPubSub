from gpspublisher.utils.utils import extract_keys, _get_fields_pynmea_parse, str_datetime_formated
from gpspublisher.utils.constants import DICT_NMEA


def filter_raw_nmea(lines, protocol=DICT_NMEA) -> dict:

    gps_info = dict(zip(extract_keys(), ""))
    li_keys_nmea = [list(ele.keys())[0] for ele in protocol]

    for line_ in lines.split('\r\n'):
        if any(cod in line_ for cod in li_keys_nmea):
            dicio_upd = _get_fields_pynmea_parse(line_)
            gps_info = {**gps_info, **dicio_upd}

            if 'error' in dicio_upd:
                datef = str_datetime_formated()
                print(f'{datef}: gps_info: error in dicio_upd '
                      f'{dicio_upd["error"]}')
    return gps_info


if __name__ == "__main__":

    lines = ("$GPVTG,140.88,T,,M,8.04,N,14.89,K,D*05\r\n"
             "$GPGGA,184353.07,1929.045,S,02410.506,"
             "E,1,04,2.6,100.00,M,-33.9,M,,0000*6D\r\n"
             "$GPRMC,123519,A,4807.038,N,01131.000,E"
             ",022.4,084.4,230394,003.1,W*6A")

    dict = filter_raw_nmea(lines)

    print(dict)
