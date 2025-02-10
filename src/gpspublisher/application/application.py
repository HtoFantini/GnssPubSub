from gpspublisher.reader.reader import GPSReader
from gpspublisher.publisher.publisher import GPSPublisher


class Gps:

    def __init__(self, configs):
        self._configs = configs
        self._publisher = GPSPublisher()
        self._reader = GPSReader(self._publisher,
                                 **self._configs)

    def get_configs(self) -> dict:
        return self._reader.get_configs()

    def start_gps_thread(self):
        self._reader.start_thread()

    def stop_gps_thread(self):
        self._reader.stop_thread()

    def get_gps(self) -> dict:
        return self._publisher.get_published_gps_data()
