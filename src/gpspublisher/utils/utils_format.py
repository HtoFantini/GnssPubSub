"""Format"""
import datetime

from gpspublisher.utils.constants import DICT_NMEA_TYPES


def format_dict_by_type(dicio_in) -> dict:
    """
    Formata os dados do GPS em um dicionario com as chaves esperadas pelo sistema

    Args:
        dicio_in (dict): Dicionario com os dados do GPS nao formatados

    Returns:
        dict: Dicionario com os dados do GPS formatados
    """
    dicio_out = {key: value for key, value in dicio_in.items() if value is not None}

    for key, expected_type in DICT_NMEA_TYPES.items():
        if key in dicio_out:
            if expected_type == 'float':
                try:
                    dicio_out[key] = float(dicio_out[key])
                except (ValueError, TypeError):
                    dicio_out[key] = 0.0
            elif expected_type == 'int':
                try:
                    dicio_out[key] = int(dicio_out[key])
                except (ValueError, TypeError):
                    dicio_out[key] = 0
            elif expected_type == 'datetime':
                if not isinstance(dicio_out[key], datetime.time):
                    dicio_out[key] = datetime.time(1, 0, 1, 10101, tzinfo=datetime.timezone.utc)
            elif key == 'Data':
                try:
                    datetime.datetime.strptime(dicio_out[key], '%Y-%m-%d')
                except Exception:
                    dicio_out[key] = '1900-01-01'

    return dicio_out


if __name__ == "__main__":

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

    dict_out = format_dict_by_type(dict_in)

    print(dict_out)
