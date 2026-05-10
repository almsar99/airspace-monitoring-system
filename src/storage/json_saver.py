import json
from pathlib import Path

from storage.base_storage import BaseStorage


class JSONSaver(BaseStorage):
    """Класс для работы с JSON-файлом."""

    def __init__(self, filename: str = "data/aeroplanes.json") -> None:
        self.__filename = filename

    def __read_data(self) -> list:
        """
        Чтение данных из файла.

        :return: list
        """
        path = Path(self.__filename)

        if not path.exists():
            return []

        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    def __write_data(self, data: list) -> None:
        """
        Запись данных в файл.

        :param data: list
        """
        path = Path(self.__filename)

        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def add(self, item) -> None:
        """
        Добавление самолета в JSON.

        :param item: Объект самолета
        """
        data = self.__read_data()

        item_dict = item.to_dict()

        if item_dict not in data:
            data.append(item_dict)

        self.__write_data(data)

    def get(self, **kwargs) -> list:
        """
        Получение данных из JSON.

        :return: list
        """
        return self.__read_data()

    def delete(self, item) -> None:
        """
        Удаление самолета из JSON.

        :param item: Объект самолета
        """
        data = self.__read_data()

        item_dict = item.to_dict()

        if item_dict in data:
            data.remove(item_dict)

        self.__write_data(data)
