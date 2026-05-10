import logging
import time

import requests

from api.base_api import BaseAPI
from config import (
    NOMINATIM_URL,
    OPENSKY_URL,
    USER_AGENT,
)
from exceptions.exceptions import (
    APIConnectionError,
    CountryNotFoundError,
)

logger = logging.getLogger(__name__)


class AeroplanesAPI(BaseAPI):
    """Класс для работы с API OpenSky и Nominatim."""

    def __init__(self) -> None:
        self.__session: requests.Session | None = None

        self.__retries = 3

        self.__timeout = 10

        self.__country_cache: dict[
            str,
            list[str],
        ] = {}

    def _connect(self) -> None:
        """Создание HTTP-сессии."""
        self.__session = requests.Session()

        logger.info("HTTP-сессия создана")

    def __get_country_coordinates(
        self,
        country: str,
    ) -> list[str]:
        """
        Получение координат страны.

        :param country: Название страны
        :return: list
        """
        self._connect()

        logger.info(f"Получение координат " f"страны: {country}")

        if country in self.__country_cache:
            logger.info("Координаты получены " "из кэша")

            return self.__country_cache[country]

        headers: dict[str, str] = {"User-Agent": USER_AGENT}

        params: dict[str, str] = {
            "country": country,
            "format": "json",
            "limit": "1",
        }

        assert self.__session is not None

        for attempt in range(self.__retries):
            try:
                response = self.__session.get(
                    NOMINATIM_URL,
                    params=params,
                    headers=headers,
                    timeout=(self.__timeout),
                )

                break

            except requests.RequestException:
                logger.warning(f"Попытка " f"{attempt + 1} " f"не удалась")

                time.sleep(1)

        else:
            raise APIConnectionError("Ошибка подключения " "к API")

        if response.status_code != 200:
            logger.error("Ошибка подключения " "к Nominatim API")

            raise APIConnectionError("Ошибка подключения " "к Nominatim API")

        data = response.json()

        if not data:
            logger.error("Страна не найдена")

            raise (CountryNotFoundError("Страна не найдена"))

        logger.info("Координаты страны " "успешно получены")

        coordinates = data[0]["boundingbox"]

        self.__country_cache[country] = coordinates

        return coordinates

    def get_data(
        self,
        country: str,
    ) -> list:
        """
        Получение данных о самолетах.

        :param country: Название страны
        :return: list
        """
        coordinates: list[str] = self.__get_country_coordinates(country)

        logger.info("Получение данных " "о самолетах")

        params: dict[str, str] = {
            "lamin": coordinates[0],
            "lamax": coordinates[1],
            "lomin": coordinates[2],
            "lomax": coordinates[3],
        }

        assert self.__session is not None

        for attempt in range(self.__retries):
            try:
                response = self.__session.get(
                    OPENSKY_URL,
                    params=params,
                    timeout=(self.__timeout),
                )

                break

            except requests.RequestException:
                logger.warning(f"Попытка " f"{attempt + 1} " f"не удалась")

                time.sleep(1)

        else:
            raise APIConnectionError("Ошибка подключения " "к API")

        if response.status_code != 200:
            logger.error("Ошибка подключения " "к OpenSky API")

            raise APIConnectionError("Ошибка подключения " "к OpenSky API")

        data = response.json()

        logger.info("Данные о самолетах " "успешно получены")

        return data.get(
            "states",
            [],
        )
