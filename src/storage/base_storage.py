from abc import ABC, abstractmethod


class BaseStorage(ABC):
    """Абстрактный класс для работы с хранилищем."""

    @abstractmethod
    def add(self, item) -> None:
        """
        Добавление объекта в хранилище.

        :param item: Объект
        """
        pass

    @abstractmethod
    def get(self, **kwargs) -> list:
        """
        Получение данных из хранилища.

        :return: list
        """
        pass

    @abstractmethod
    def delete(self, item) -> None:
        """
        Удаление объекта из хранилища.

        :param item: Объект
        """
        pass
