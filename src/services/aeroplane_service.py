from api.aeroplanes_api import AeroplanesAPI
from models.aeroplane import Aeroplane
from storage.json_saver import JSONSaver
from utils.filters import (
    filter_by_country,
    get_top_aeroplanes,
    sort_by_altitude,
)


class AeroplaneService:
    """Сервис для работы с самолетами."""

    def __init__(self) -> None:
        self.__api = AeroplanesAPI()

        self.__storage = JSONSaver()

    def get_aeroplanes(
        self,
        country: str,
    ) -> list[Aeroplane]:
        """
        Получение самолетов.

        :param country: str
        :return: list[Aeroplane]
        """
        raw_data = self.__api.get_data(country)

        aeroplanes = Aeroplane.cast_to_object_list(raw_data)

        for aeroplane in aeroplanes:
            self.__storage.add(aeroplane)

        return aeroplanes

    @staticmethod
    def get_top_by_altitude(
        aeroplanes: list[Aeroplane],
        top_n: int,
    ) -> list[Aeroplane]:
        """
        Получение топа самолетов.

        :param aeroplanes: list
        :param top_n: int
        :return: list[Aeroplane]
        """
        sorted_aeroplanes = sort_by_altitude(aeroplanes)

        return get_top_aeroplanes(
            sorted_aeroplanes,
            top_n,
        )

    @staticmethod
    def filter_by_registration_country(
        aeroplanes: list[Aeroplane],
        countries: list[str],
    ) -> list[Aeroplane]:
        """
        Фильтрация самолетов.

        :param aeroplanes: list
        :param countries: list
        :return: list[Aeroplane]
        """
        return filter_by_country(
            aeroplanes,
            countries,
        )
