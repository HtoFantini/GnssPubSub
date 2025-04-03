from gpspublisher.utils.utils import _get_fields_pynmea_parse


def test_invalid_latitude_longitude_checksum_error():

    # CHECKSUM ERROR
    checksum_error_line = "$GPGGA,123519,,,,1,12,1.0,10.0,M,46.9,M,,*47"

    # Chama a função que deve processar o dado corrompido
    assert _get_fields_pynmea_parse(checksum_error_line) == {}


def test_invalid_latitude_longitude_stopit_error():

    # corrupt_data = '$$xb bʒr  bbbbbbR  jR":     q '

    # StopIteration forced error
    stopit_error_line = "$GPGLL,4916.45,N,12311.12,W,225444,A,*1D"

    # Chama a função que deve processar o dado corrompido
    assert _get_fields_pynmea_parse(stopit_error_line) == {}


def test_invalid_latitude_longitude_parse_error():

    corrupt_data = '$$xb bʒr  bbbbbbR  jR":     q '

    # Chama a função que deve processar o dado corrompido
    assert _get_fields_pynmea_parse(corrupt_data) == {}
