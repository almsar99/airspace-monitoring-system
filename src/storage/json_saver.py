import json
from datetime import datetime
from pathlib import Path

from storage.base_storage import BaseStorage


class JSONSaver(BaseStorage):
    """Класс для работы с JSON-файлом."""

    def __init__(
        self,
        filename: str = "data/aeroplanes.json",
    ) -> None:
        self.__filename = filename

    def __read_data(self) -> list:
        """
        Чтение данных из файла.

        :return: list
        """
        path = Path(self.__filename)

        if not path.exists():
            return []

        with open(
            path,
            "r",
            encoding="utf-8",
        ) as file:
            return json.load(file)

    def __write_data(
        self,
        data: list,
    ) -> None:
        """
        Запись данных в файл.

        :param data: list
        """
        path = Path(self.__filename)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(
            path,
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False,
            )

    def save(
        self,
        aeroplanes: list,
    ) -> None:
        """
        Сохранение списка самолетов.

        :param aeroplanes: list
        """
        data = []

        for aeroplane in aeroplanes:
            aeroplane_dict = aeroplane.to_dict()

            aeroplane_dict["created_at"] = datetime.now().isoformat()

            data.append(aeroplane_dict)

        self.__write_data(data)

    def add(
        self,
        item,
    ) -> None:
        """
        Добавление самолета в JSON.

        :param item: Объект самолета
        """
        data = self.__read_data()

        item_dict = item.to_dict()

        item_dict["created_at"] = datetime.now().isoformat()

        aeroplane_exists = any(
            plane["callsign"] == item_dict["callsign"] for plane in data
        )

        if not aeroplane_exists:
            data.append(item_dict)

        self.__write_data(data)

    def get(
        self,
        **kwargs,
    ) -> list:
        """
        Получение данных из JSON.

        :return: list
        """
        return self.__read_data()

    def delete(
        self,
        item,
    ) -> None:
        """
        Удаление самолета из JSON.

        :param item: Объект самолета
        """
        data = self.__read_data()

        item_dict = item.to_dict()

        updated_data = [
            plane for plane in data if plane["callsign"] != item_dict["callsign"]
        ]

        self.__write_data(updated_data)
