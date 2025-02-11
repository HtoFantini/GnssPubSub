"""Test Configuracao dinamica do device"""
from unittest.mock import MagicMock, patch
import pytest

from gpspublisher.reader.reader import GPSReader
from gpspublisher.devices import gps_devices
from gpspublisher.application.application import Gps


def test_gpsreader_missing_read_time():
    """
    Testa o tratamento de erro na classe GPSReader caso falte o parametro \
        de configuracao 'read_time'
    """
    publisher = MagicMock()
    config = {"device": "Neo6M"}
    with pytest.raises(KeyError):
        GPSReader(publisher, **config).target_read_loop()


def test_gpsreader_missing_device():
    """
    Testa o tratamento de erro na classe GPSReader caso falte o parametro \
        de configuracao 'device'
    """
    publisher = MagicMock()
    config = {"read_time": 1}
    with pytest.raises(KeyError):
        GPSReader(publisher, **config).target_read_loop()


def test_gpsreader_invalid_device():
    """
    Testa o tratamento de erro na classe GPSReader caso o parametro de \
          configuracao 'device' nao bata com um existente
    """
    publisher = MagicMock()
    config = {"read_time": 1, "device": "UnknownDevice"}
    with pytest.raises(ValueError, match="Device 'UnknownDevice' não reconhecido"):
        GPSReader(publisher, **config).target_read_loop()


def test_gpsreader_valid_device():
    """
    Testa o comportamento do sistema caso ambos os parametros de configuracao \
        estejam corretos
    """
    publisher = MagicMock()
    config = {"read_time": 1, "device": "Neo6M"}

    with patch.object(gps_devices, "Neo6M", MagicMock()) as mock_device_class:
        gps_reader = GPSReader(publisher, **config)
        gps_reader.stop_thread()
        gps_reader.target_read_loop()
        mock_device_class.assert_called_once()


def test_configs_forwarding_gps_to_gpsreader():
    """
    Testa se a classe Gps passa corretamente as configurações para a GPSReader
    """
    configs = {"read_time": 1, "device": "Neo6M"}

    gps = Gps(configs)

    # Obtém as configurações que chegaram ao GPSReader
    reader_configs = gps.get_configs()

    assert reader_configs == configs, f"As configurações esperadas eram \
                                            {configs}, mas foram {reader_configs}"
