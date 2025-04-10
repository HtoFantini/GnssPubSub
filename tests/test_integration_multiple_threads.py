import threading
import time
import serial

from unittest.mock import MagicMock, patch

from gpspublisher.application.application import Gps


def test_multiplos_cliente_gps_Neo6M(monkeypatch, n_threads=1000):
    """ Teste sistêmico para validar o fluxo completo do GPS """
    # Mock da serial.Serial

    mock_serial = MagicMock()
    monkeypatch.setattr(serial, 'Serial', mock_serial)

    configs = {"read_time": 0.1, "device": "Neo6M"}

    lines = (
        "$GPVTG,140.88,T,,M,8.04,N,14.89,K,D*05\r\n"
        "$GPGGA,184353.07,1929.045,S,02410.506,"
        "E,1,04,2.6,100.00,M,-33.9,M,,0000*6D\r\n"
        "$GPRMC,123519,A,4807.038,N,01131.000,E"
        ",022.4,084.4,230394,003.1,W*6A"
    )

    # Caso seja desejado o teste sistemico em outro device, basta substituir \
    # o 'Neo6m' na linha imediatameante abaixo pelo nome do device
    with patch("gpspublisher.devices.gps_devices.Neo6M.read_raw_data",
               return_value=lines):
        # Cria uma instância do Gps
        gps = Gps(configs)

        # Inicia a thread de leitura do GPS
        gps.start_gps_thread()
        time.sleep(0.5)

        # Simula um cliente obtendo o dado
        def client(result_list, index):
            result_list[index] = gps.get_gps()
            # time.sleep(5)

        threads = []
        results = [None] * n_threads

        # Cria 10 threads de cliente solicitando o dado publicado
        for i in range(n_threads):
            t = threading.Thread(target=client, args=(results, i))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        for data in results:
            assert data is not None, "Alguma thread não conseguiu acessar os dados do GPS"
            assert isinstance(data, dict), "O dado de GPS deveria ser um dicionário"
            assert bool(data), "O dicionário 'data' está vazio"

        gps.stop_gps_thread()
        time.sleep(0.2)
