"""Test Formatacao dos dados conforme o tipo desejado"""
import datetime

from gpspublisher.utils.utils_format import format_dict_by_type


def test_format_by_type_wrong_values():

    dict_in = {
        'Velocidade': 'awd',
        'Direcao_deslocamento_graus_norte': None,
        'Data_hora_UTC': 'd',
        'Latitude': 48,
        'Longitude': None,
        'Altitude': '1900-01-01',
        'Indicador_qualidade_GPS': 'one',
        'Numero_Satelites_Utilizado': 3.5,
        'Data': '2025-02'
    }

    expected_dict_out = {
        'Velocidade': 0.0,
        'Data_hora_UTC': datetime.time(1, 0, 1, 10101, tzinfo=datetime.timezone.utc),
        'Latitude': 48.0,
        'Altitude': 0.0,
        'Indicador_qualidade_GPS': 0,
        'Numero_Satelites_Utilizado': 3,
        'Data': '1900-01-01'

    }

    dict_out = format_dict_by_type(dict_in)

    assert dict_out == expected_dict_out


def test_format_by_type_correct_values():

    dict_in = {
        'Velocidade': 1.123,
        'Direcao_deslocamento_graus_norte': 32.10,
        'Data_hora_UTC': datetime.time(18, 43, 53, 70000, tzinfo=datetime.timezone.utc),
        'Latitude': 48.13,
        'Longitude': 13.48,
        'Altitude': 700.4,
        'Indicador_qualidade_GPS': 1,
        'Numero_Satelites_Utilizado': 5,
        'Data': '2025-02-07'
    }

    expected_dict_out = {
        'Velocidade': 1.123,
        'Direcao_deslocamento_graus_norte': 32.10,
        'Data_hora_UTC': datetime.time(18, 43, 53, 70000, tzinfo=datetime.timezone.utc),
        'Latitude': 48.13,
        'Longitude': 13.48,
        'Altitude': 700.4,
        'Indicador_qualidade_GPS': 1,
        'Numero_Satelites_Utilizado': 5,
        'Data': '2025-02-07'

    }

    dict_out = format_dict_by_type(dict_in)

    assert dict_out == expected_dict_out
