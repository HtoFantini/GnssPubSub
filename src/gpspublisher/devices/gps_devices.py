import datetime

from gpspublisher.devices.interface_device import Device
from gpspublisher.utils.utils import get_gps_nmea_info_serial
from gpspublisher.utils.constants import DICT_NMEA, DICT_DEFAULT_PORTS


class Neo6M(Device):
    """Classe para obtenção dos dados do GPS Neo-6m
    """

    def __init__(self):
        _protocol = DICT_NMEA
        _baudrate = 9600
        _port = DICT_DEFAULT_PORTS["Serial"]
        super().__init__(_protocol, _baudrate, _port)

    def read_raw_data(self):
        return get_gps_nmea_info_serial(protocol=self._protocol, baudrate=self._baudrate, serial_port=self._port)

    # TODO Principio de Responsabilidade Única (read_raw_data: str, filter_raw_data, format_data)
    def filtered_gps_data(self):
        # TODO from here: format_data(dict) -> dict* formatado
        dicio_out = {key: value for key, value in self.read_raw_data().items() if value is not None}

        for key in dicio_out:
            if key == 'Data':
                try:
                    datetime.datetime.strptime(dicio_out['Data'], '%Y-%m-%d')
                except Exception:
                    dicio_out['Data'] = '1900-01-01'
            if key == 'Data_hora_UTC':
                if not isinstance(dicio_out['Data_hora_UTC'], datetime.time):
                    dicio_out['Data_hora_UTC'] = datetime.time(1, 0, 1, 10101, tzinfo=datetime.timezone.utc)
        return dicio_out
