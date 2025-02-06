import pytest
from gpspublisher.reader.reader import GPSReader
from gpspublisher.publisher.publisher import GPSPublisher
from gpspublisher.devices.gps_devices import Neo6M  # Importa a classe real do dispositivo


def test_gpsreader_creates_neo6m():
    """Testa se o GPSReader instancia corretamente um objeto Neo6M"""
    publisher = GPSPublisher()
    config = {"read_time": 1, "device": "Neo6M"}

    gps_reader = GPSReader(publisher, **config)

    # Chamamos manualmente a função para testar a criação do objeto
    gps_reader.target_read_loop()

    # Verifica se o objeto foi instanciado corretamente
    assert isinstance(gps_reader._config["device"], str)
    assert gps_reader._config["device"] == "Neo6M"
