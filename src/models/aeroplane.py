from typing import List


class Aeroplane:
    """Класс самолета."""

    __slots__ = (
        "_callsign",
        "_country",
        "_velocity",
        "_altitude",
    )

    def __init__(
        self,
        callsign: str,
        country: str,
        velocity: float,
        altitude: float,
    ) -> None:
        self._callsign = self.__validate_string(callsign)
        self._country = self.__validate_string(country)
        self._velocity = self.__validate_number(velocity)
        self._altitude = self.__validate_number(altitude)

    @property
    def callsign(self) -> str:
        return self._callsign

    @property
    def country(self) -> str:
        return self._country

    @property
    def velocity(self) -> float:
        return self._velocity

    @property
    def altitude(self) -> float:
        return self._altitude

    def __lt__(self, other: "Aeroplane") -> bool:
        """Сравнение самолетов по высоте."""
        return self.altitude < other.altitude

    def __gt__(self, other: "Aeroplane") -> bool:
        """Сравнение самолетов по высоте."""
        return self.altitude > other.altitude

    def __eq__(self, other: object) -> bool:
        """Сравнение самолетов по высоте."""
        if not isinstance(other, Aeroplane):
            return NotImplemented

        return self.altitude == other.altitude

    def __repr__(self) -> str:
        return (
            f"{self.callsign} | "
            f"{self.country} | "
            f"Speed: {self.velocity} m/s | "
            f"Altitude: {self.altitude} m"
        )

    @staticmethod
    def cast_to_object_list(data: list) -> List["Aeroplane"]:
        """
        Преобразование данных API в список объектов.

        :param data: list
        :return: list[Aeroplane]
        """
        aeroplanes = []

        for item in data:
            callsign = item[1] or "Unknown"
            country = item[2] or "Unknown"
            velocity = item[9] or 0.0
            altitude = item[13] or 0.0

            aeroplane = Aeroplane(
                callsign,
                country,
                velocity,
                altitude,
            )

            aeroplanes.append(aeroplane)

        return aeroplanes

    def to_dict(self) -> dict:
        """
        Преобразование объекта в словарь.

        :return: dict
        """
        return {
            "callsign": self.callsign,
            "country": self.country,
            "velocity": self.velocity,
            "altitude": self.altitude,
        }

    @staticmethod
    def __validate_string(value: str) -> str:
        """
        Валидация строки.

        :param value: str
        :return: str
        """
        if not isinstance(value, str):
            raise TypeError("Значение должно быть строкой")

        return value.strip()

    @staticmethod
    def __validate_number(value: float) -> float:
        """
        Валидация числа.

        :param value: float
        :return: float
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом")

        return float(value)
