"Test filtro de dados crus com padrao nmea"
import datetime

from gpspublisher.utils.utils_filter import filter_raw_nmea


def test_filter_complete_nmea_raw_data_():

    lines = ("$GPVTG,140.88,T,,M,8.04,N,14.89,K,D*05\r\n"
             "$GPGGA,184353.07,1929.045,S,02410.506,"
             "E,1,04,2.6,100.00,M,-33.9,M,,0000*6D\r\n"
             "$GPRMC,123519,A,4807.038,N,01131.000,E"
             ",022.4,084.4,230394,003.1,W*6A")

    expected_dict_out = {
        'Velocidade': 41.4848,
        'Direcao_deslocamento_graus_norte': 140.88,
        'Data_hora_UTC': datetime.time(18, 43, 53, 70000, tzinfo=datetime.timezone.utc),
        'Latitude': 48.1173,
        'Longitude': 11.516666666666667,
        'Altitude': 100.0,
        'Indicador_qualidade_GPS': 1,
        'Numero_Satelites_Utilizado': '04',
        'Data': '1994-03-23'
    }

    dict_out = filter_raw_nmea(lines)

    assert expected_dict_out == dict_out


def test_filter_incomplete_nmea_raw_data_():

    lines = ("$GPVTG,,,,,,,,14.89,K,D*05\r\n"
             "$GPGGA,184353.07,1929.045,S,02410.506,"
             "E,1,04,2.6,100.00,M,-33.9,M,,0000*6D\r\n"
             "$GPRMC,,A,4807.038,N,01131.000,E"
             ",022.4,084.4,230394,003.1,W*6A")

    expected_dict_out = {
        'Data_hora_UTC': datetime.time(18, 43, 53, 70000, tzinfo=datetime.timezone.utc),
        'Latitude': -19.484083333333334,
        'Longitude': 24.1751,
        'Altitude': 100.0,
        'Indicador_qualidade_GPS': 1,
        'Numero_Satelites_Utilizado': '04'
    }

    dict_out = filter_raw_nmea(lines)

    assert expected_dict_out == dict_out
