"""Device minimum methods"""
from abc import ABC, abstractmethod


class Device(ABC):
    """Classe abstrata com as funcoes base para qualuqer device criado

    Args:
        ABC (_type_): _description_
    """

    def __init__(self, protocol, baudrate, port, port_obj):
        self._protocol = protocol
        self._baudrate = baudrate
        self._port = port
        self._port_obj = port_obj

    @abstractmethod
    def read_raw_data(self, port_obj) -> str:
        """Reads raw data from the device.

        Returns:
            str: Raw data read from the device in string format.
        """

    @abstractmethod
    def filter_raw_data(self, raw_lines) -> dict:
        """Filters and processes the raw data read from the device

        Args:
            raw_lines (str): Raw data read from the device in string format.

        Returns:
            dict: Filtered and processed data in dictionary format.
        """

    @abstractmethod
    def format_gps_data(self, dicio_in) -> dict:
        """Formats the GPS data to the expected output format

        Args:
            dicio_in (dict): Filtered and processed data in dictionary format.

        Returns:
            dict: Formatted GPS data in dictionary format.
        """
