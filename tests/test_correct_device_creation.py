import pytest
from gpspublisher.reader.reader import GPSReader
from gpspublisher.publisher.publisher import GPSPublisher
from gpspublisher.devices import gps_devices


def test_gpsreader_creates_Neo6M_device():
    """
    Testa se o GPSReader cria corretamente o objeto `dev_obj` com base no nome do dispositivo no config
    """

    publisher = GPSPublisher()
    config = {"read_time": 1, "device": "Neo6M"}

    gps_reader = GPSReader(publisher, **config)

    gps_reader._stop_flag.set()

    gps_reader.target_read_loop()

    assert isinstance(gps_reader._config["device"], str)
    assert gps_reader._config["device"] == "Neo6M"

    dev_class = getattr(gps_devices, "Neo6M")
    dev_obj = dev_class()
    assert isinstance(dev_obj, gps_devices.Neo6M)
