"""Devices"""
import serial

from gpspublisher.devices.interface_device import Device
from gpspublisher.utils.utils_read import read_raw_serial
from gpspublisher.utils.utils_filter import filter_raw_nmea
from gpspublisher.utils.utils_format import format_dict_by_type
from gpspublisher.utils.constants import DICT_NMEA, DICT_DEFAULT_PORTS


class Neo6M(Device):
    """
    Classe para obtenção dos dados do GPS Neo-6m
    """

    def __init__(self):
        _protocol = DICT_NMEA
        _baudrate = 9600
        _port = DICT_DEFAULT_PORTS["Serial"]
        _port_obj = serial.Serial(_port, _baudrate, timeout=1,
                                  bytesize=serial.EIGHTBITS,
                                  parity=serial.PARITY_NONE,
                                  stopbits=serial.STOPBITS_ONE)

        super().__init__(_protocol, _baudrate, _port, _port_obj)

    def read_raw_data(self) -> str:
        return read_raw_serial(serial_obj=self._port_obj)

    def filter_raw_data(self, raw_lines) -> dict:
        return filter_raw_nmea(lines=raw_lines, protocol=self._protocol)

    def format_gps_data(self, dicio_in) -> dict:
        return format_dict_by_type(dicio_in=dicio_in)
