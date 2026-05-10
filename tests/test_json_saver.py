from storage.json_saver import JSONSaver
from models.aeroplane import Aeroplane


def test_add_aeroplane():
    saver = JSONSaver("data/test.json")

    aeroplane = Aeroplane(
        "DLH123",
        "Germany",
        250,
        10000,
    )

    saver.add(aeroplane)

    data = saver.get()

    assert len(data) > 0
