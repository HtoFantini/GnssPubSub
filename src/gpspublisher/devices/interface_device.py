from abc import ABC, abstractmethod


class Device(ABC):
    """_summary_

    Args:
        ABC (_type_): _description_
    """

    def __init__(self, protocol, baudrate, port):
        self._protocol = protocol
        self._baudrate = baudrate
        self._port = port

    @abstractmethod
    def read_raw_data(self):
        pass

    @abstractmethod
    def filtered_gps_data(self):
        pass
