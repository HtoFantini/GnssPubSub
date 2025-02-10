import threading
import time

from gpspublisher.devices import gps_devices


class GPSReader:
    """Classe que faz a leitura continua dos dados de gps fornecidos pelo device
    """

    def __init__(self, publisher, **kwargs):
        self._publisher = publisher
        self._config = kwargs
        self._thr = threading.Thread(
            target=self.target_read_loop, daemon=True
        )
        self._stop_flag = threading.Event()

    def get_configs(self):
        return self._config

    def start_thread(self):
        """Encapsulamento para inicialização da thread
        """
        self._stop_flag.clear()
        self._thr.start()

    def stop_thread(self):
        """Set do evento que para a execução da thread
        """
        self._stop_flag.set()

    def target_read_loop(self):
        """Loop que le o arquivo de configuracao e mantem a leitura dos dados \
            de gps do device continuamente
        """
        try:
            read_time = self._config["read_time"]
            device_name = self._config["device"]

        except KeyError as ke:
            raise KeyError(f"Erro: Constant {ke.args[0]} not found in config file")

        try:
            dev_class = getattr(gps_devices, device_name)
            dev_obj = dev_class()
        except AttributeError:
            raise ValueError(f"Device '{device_name}' não reconhecido")

        while not self._stop_flag.is_set():
            # TODO: explicit call read/filter/format
            f_gps_data = dev_obj.filtered_gps_data()
            self._publisher.publish_gps_data(f_gps_data)
            # read, filter and format data from port
            raw_data = dev_obj.read_raw_data()
            dict_filtered_raw = dev_obj.filter_raw_data(raw_data)
            dict_formated_data = dev_obj.format_gps_data(dict_filtered_raw)

            self._publisher.publish_gps_data(dict_formated_data)
            time.sleep(read_time)
