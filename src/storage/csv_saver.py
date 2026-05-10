import csv
from pathlib import Path

from models.aeroplane import Aeroplane


class CSVSaver:
    """Сохранение самолетов в CSV."""

    def __init__(
        self,
        filename: str = ("data/aeroplanes.csv"),
    ) -> None:
        self.__filename = filename

    def save(
        self,
        aeroplanes: list[Aeroplane],
    ) -> None:
        """
        Сохранение самолетов.

        :param aeroplanes: list
        """
        path = Path(self.__filename)

        with open(
            path,
            "w",
            newline="",
            encoding="utf-8",
        ) as file:
            writer = csv.writer(file)

            writer.writerow(
                [
                    "callsign",
                    "country",
                    "velocity",
                    "altitude",
                ]
            )

            for aeroplane in aeroplanes:
                writer.writerow(
                    [
                        aeroplane.callsign,
                        aeroplane.country,
                        aeroplane.velocity,
                        aeroplane.altitude,
                    ]
                )
