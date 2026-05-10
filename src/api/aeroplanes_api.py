import requests

from api.base_api import BaseAPI


class AeroplanesAPI(BaseAPI):
    """Класс для работы с API OpenSky и Nominatim."""

    __BASE_NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
    __BASE_OPENSKY_URL = "https://opensky-network.org/api/states/all"

    def __init__(self) -> None:
        self.__session = None

    def _connect(self) -> None:
        """Создание HTTP-сессии."""
        self.__session = requests.Session()

    def __get_country_coordinates(self, country: str) -> list:
        """
        Получение координат страны.

        :param country: Название страны
        :return: list
        """
        self._connect()

        headers = {
            "User-Agent": "airspace-monitoring-system"
        }

        params = {
            "country": country,
            "format": "json",
            "limit": 1,
        }

        response = self.__session.get(
            self.__BASE_NOMINATIM_URL,
            params=params,
            headers=headers,
        )

        if response.status_code != 200:
            raise ConnectionError("Ошибка подключения к Nominatim API")

        data = response.json()

        if not data:
            raise ValueError("Страна не найдена")

        return data[0]["boundingbox"]

    def get_data(self, country: str) -> list:
        """
        Получение данных о самолетах.

        :param country: Название страны
        :return: list
        """
        coordinates = self.__get_country_coordinates(country)

        params = {
            "lamin": coordinates[0],
            "lamax": coordinates[1],
            "lomin": coordinates[2],
            "lomax": coordinates[3],
        }

        response = self.__session.get(
            self.__BASE_OPENSKY_URL,
            params=params,
        )

        if response.status_code != 200:
            raise ConnectionError("Ошибка подключения к OpenSky API")

        data = response.json()

        return data.get("states", [])
