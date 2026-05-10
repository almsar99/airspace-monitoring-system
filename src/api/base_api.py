from abc import ABC, abstractmethod


class BaseAPI(ABC):
    """Абстрактный класс для работы с API."""

    @abstractmethod
    def _connect(self) -> None:
        """Подключение к API."""
        pass

    @abstractmethod
    def get_data(self, country: str) -> list:
        """
        Получение данных о самолетах.

        :param country: Название страны
        :return: list
        """
        pass
