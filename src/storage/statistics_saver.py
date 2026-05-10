import json
from pathlib import Path


class StatisticsSaver:
    """Сохранение статистики."""

    def __init__(
        self,
        filename: str = ("data/statistics.json"),
    ) -> None:
        self.__filename = filename

    def save(
        self,
        statistics: dict,
    ) -> None:
        """
        Сохранение статистики.

        :param statistics: dict
        """
        path = Path(self.__filename)

        with open(
            path,
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                statistics,
                file,
                indent=4,
                ensure_ascii=False,
            )
