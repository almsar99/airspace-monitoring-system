import pytest

from storage.base_storage import BaseStorage
from storage.json_saver import JSONSaver
from models.aeroplane import Aeroplane


def test_base_storage_methods():
    methods = [
        "add",
        "get",
        "delete",
    ]

    for method in methods:
        assert hasattr(BaseStorage, method)


def test_json_saver_get_empty(tmp_path):
    file_path = tmp_path / "test.json"

    saver = JSONSaver(str(file_path))

    result = saver.get()

    assert result == []


def test_json_saver_delete(tmp_path):
    file_path = tmp_path / "test.json"

    saver = JSONSaver(str(file_path))

    aeroplane = Aeroplane(
        "DLH123",
        "Germany",
        250,
        10000,
    )

    saver.add(aeroplane)

    saver.delete(aeroplane)

    result = saver.get()

    assert result == []


def test_json_saver_add_multiple(tmp_path):
    file_path = tmp_path / "test.json"

    saver = JSONSaver(str(file_path))

    first = Aeroplane(
        "AAA",
        "Germany",
        100,
        1000,
    )

    second = Aeroplane(
        "BBB",
        "France",
        200,
        2000,
    )

    saver.add(first)
    saver.add(second)

    result = saver.get()

    assert len(result) == 2


def test_base_storage_instance():
    with pytest.raises(TypeError):
        BaseStorage()
