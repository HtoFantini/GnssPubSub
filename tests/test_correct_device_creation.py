"""Test Criação do Device"""
import serial

from unittest.mock import MagicMock
from gpspublisher.reader.reader import GPSReader
from gpspublisher.publisher.publisher import GPSPublisher
from gpspublisher.devices import gps_devices


def test_gpsreader_creates_Neo6M_device(monkeypatch):
    """
    Testa se o GPSReader cria corretamente o objeto `dev_obj` com base no \
        nome do dispositivo no parametro de configuracao 'device'
    """

    # Mock da serial.Serial
    mock_serial = MagicMock()
    monkeypatch.setattr(serial, 'Serial', mock_serial)

    dev_name = "Neo6M"
    publisher = GPSPublisher()
    config = {"read_time": 1, "device": dev_name}

    gps_reader = GPSReader(publisher, **config)

    gps_reader.stop_thread()

    gps_reader.target_read_loop()

    reader_config = gps_reader.get_configs()

    assert reader_config["device"] == dev_name

    dev_class = getattr(gps_devices, dev_name)
    dev_obj = dev_class()
    assert isinstance(dev_obj, gps_devices.Neo6M)
