"""Test Leitura de portas"""
from gpspublisher.utils.utils_read import read_raw_serial


def test_read_raw_serial_returns_string(test=True):
    """
    Testa se a função read_raw_serial retorna uma string com os dados \
        simulados da porta serial.
    """
    # Dados simulados que a função serial.read() deve retornar
    mock_serial_data = (
        b"$GPVTG,140.88,T,,M,8.04,N,14.89,K,D*05\r\n"
        b"$GPGGA,184353.07,1929.045,S,02410.506,"
        b"E,1,04,2.6,100.00,M,-33.9,M,,0000*6D\r\n"
        b"$GPRMC,123519,A,4807.038,N,01131.000,E"
        b",022.4,084.4,230394,003.1,W*6A         "
    )

    result = read_raw_serial(test=test)

    # Verifica se o resultado é uma string
    assert isinstance(result, str), "A função não retornou uma string"

    # Verifica se o conteúdo da string está correto
    expected_output = mock_serial_data.decode("utf-8").strip()
    assert result == expected_output, "O conteúdo da string não corresponde ao esperado"
