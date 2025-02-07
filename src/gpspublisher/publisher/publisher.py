import threading


class GPSPublisher:
    """Classe que armazena, publica e retorna o ultimo dado de GPS fornecido
    """

    def __init__(self):
        self._gps_data = {}
        self._lock = threading.Lock()

    def publish_gps_data(self, gps_data):
        """Publica o dado de GPS mais recente

        Args:
            gps_data (_type_): dado de GPS recebido
        """
        # TODO priority writer over reader
        with self._lock:
            self._gps_data = gps_data

    def get_gps_data(self):
        """Retorna o ultimo dado de GPS publicado
        """
        with self._lock:
            return self._gps_data
