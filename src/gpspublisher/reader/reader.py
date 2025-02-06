import threading
import time

from gpspublisher.devices import gps_devices


class GPSReader:
    """_summary_
    """

    def __init__(self, publisher, **kwargs):
        self._publisher = publisher
        self._config = kwargs
        self._thr = threading.Thread(
            target=self.target_read_loop, daemon=True
        )
        self._stop_flag = threading.Event()

    def start_thread(self):
        """_summary_
        """
        self._thr.start()

    def stop_thread(self):
        """_summary_
        """
        self._stop_flag.set()

    def target_read_loop(self):
        """_summary_
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
            f_gps_data = dev_obj.filtered_gps_data()
            self._publisher.publish_gps_data(f_gps_data)
            time.sleep(read_time)
