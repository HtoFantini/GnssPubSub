"Test Configuracao dinamica do device"
import pytest
from unittest.mock import MagicMock, patch
from gpspublisher.reader.reader import GPSReader
from gpspublisher.devices import gps_devices


def test_gpsreader_missing_read_time():
    publisher = MagicMock()
    config = {"device": "Neo6M"}
    with pytest.raises(KeyError):
        GPSReader(publisher, **config).target_read_loop()


def test_gpsreader_missing_device():
    publisher = MagicMock()
    config = {"read_time": 1}
    with pytest.raises(KeyError):
        GPSReader(publisher, **config).target_read_loop()


def test_gpsreader_invalid_device():
    publisher = MagicMock()
    config = {"read_time": 1, "device": "UnknownDevice"}
    with pytest.raises(ValueError, match="Device 'UnknownDevice' não reconhecido"):
        GPSReader(publisher, **config).target_read_loop()


def test_gpsreader_valid_device():
    publisher = MagicMock()
    config = {"read_time": 1, "device": "Neo6M"}

    with patch.object(gps_devices, "Neo6M", MagicMock()) as mock_device_class:
        gps_reader = GPSReader(publisher, **config)
        gps_reader._stop_flag.set()
        gps_reader.target_read_loop()
        mock_device_class.assert_called_once()
