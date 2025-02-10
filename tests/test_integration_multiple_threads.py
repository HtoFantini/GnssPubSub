import threading
import time
from gpspublisher.application.application import Gps


def test_multiplos_cliente_gps(n_threads=1000):
    """ Teste sistêmico para validar o fluxo completo do GPS """

    configs = {"read_time": 0.1, "device": "Neo6M"}
    gps = Gps(configs)

    # Inicia thread de leitura da porta
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

    gps.stop_gps_thread()
    time.sleep(0.2)
