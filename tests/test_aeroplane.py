import pytest

from models.aeroplane import Aeroplane


def test_aeroplane_init():
    aeroplane = Aeroplane(
        "DLH123",
        "Germany",
        250.0,
        10000.0,
    )

    assert aeroplane.callsign == "DLH123"
    assert aeroplane.country == "Germany"
    assert aeroplane.velocity == 250.0
    assert aeroplane.altitude == 10000.0


def test_aeroplane_compare():
    first = Aeroplane(
        "AAA",
        "Germany",
        200,
        10000,
    )

    second = Aeroplane(
        "BBB",
        "France",
        300,
        12000,
    )

    assert second > first


def test_invalid_velocity():
    with pytest.raises(TypeError):
        Aeroplane(
            "AAA",
            "Germany",
            "fast",
            1000,
        )


def test_invalid_altitude():
    with pytest.raises(TypeError):
        Aeroplane(
            "AAA",
            "Germany",
            100,
            "high",
        )
