import logging

from rich.console import Console
from rich.table import Table

from api.aeroplanes_api import (
    AeroplanesAPI,
)
from config import (
    LOG_FILE,
    LOG_LEVEL,
)
from models.aeroplane import (
    Aeroplane,
)
from services.aeroplane_service import (
    AeroplaneService,
)
from storage.csv_saver import (
    CSVSaver,
)
from storage.json_saver import (
    JSONSaver,
)
from storage.statistics_saver import (
    StatisticsSaver,
)
from utils.statistics import (
    get_average_altitude,
    get_average_velocity,
    get_max_altitude,
)

logging.basicConfig(
    level=LOG_LEVEL,
    filename=LOG_FILE,
    filemode="a",
    format=("%(asctime)s | " "%(levelname)s | " "%(message)s"),
)

logger = logging.getLogger(__name__)

console = Console()


def print_aeroplanes(
    aeroplanes: list[Aeroplane],
) -> None:
    """
    Вывод самолетов в таблице.

    :param aeroplanes: list
    """
    table = Table(title="Airspace Monitoring")

    table.add_column("Callsign")

    table.add_column("Country")

    table.add_column("Velocity")

    table.add_column("Altitude")

    for aeroplane in aeroplanes:
        table.add_row(
            aeroplane.callsign,
            aeroplane.country,
            str(aeroplane.velocity),
            str(aeroplane.altitude),
        )

    console.print(table)


def user_interaction() -> None:
    """Функция взаимодействия с пользователем."""
    country = input("Введите название страны: ")

    logger.info("Получен запрос пользователя")

    api = AeroplanesAPI()

    try:
        data = api.get_data(country)

        aeroplanes = Aeroplane.cast_to_object_list(data)

        logger.info("Данные успешно получены")

    except Exception as error:
        logger.error(error)

        print(f"Ошибка: {error}")

        return

    service = AeroplaneService()

    print(f"\nНайдено самолетов: " f"{len(aeroplanes)}")

    average_altitude = get_average_altitude(aeroplanes)

    average_velocity = get_average_velocity(aeroplanes)

    max_altitude = get_max_altitude(aeroplanes)

    statistics = {
        "average_altitude": average_altitude,
        "average_velocity": average_velocity,
        "max_altitude": max_altitude,
        "total_aeroplanes": len(aeroplanes),
    }

    statistics_saver = StatisticsSaver()

    statistics_saver.save(statistics)

    csv_saver = CSVSaver()

    csv_saver.save(aeroplanes)

    json_saver = JSONSaver()

    json_saver.save(aeroplanes)

    logger.info("Статистика успешно " "сохранена")

    logger.info("CSV файл успешно " "сохранен")

    logger.info("JSON файл успешно " "сохранен")

    print("\nСтатистика:\n")

    print(f"Средняя высота: " f"{average_altitude:.2f} m")

    print(f"Средняя скорость: " f"{average_velocity:.2f} m/s")

    print(f"Максимальная высота: " f"{max_altitude:.2f} m")

    top_n = int(input("\nВведите количество " "самолетов для топа: "))

    top_aeroplanes = service.get_top_by_altitude(
        aeroplanes,
        top_n,
    )

    print("\nТоп самолетов " "по высоте:\n")

    print_aeroplanes(top_aeroplanes)

    countries_input = input("\nВведите страны регистрации " "через запятую: ")

    countries = countries_input.split(",")

    countries = [country.strip() for country in countries]

    filtered_aeroplanes = service.filter_by_registration_country(
        aeroplanes,
        countries,
    )

    print("\nСамолеты по стране " "регистрации:\n")

    print_aeroplanes(filtered_aeroplanes)

    logger.info("Программа успешно " "завершена")


if __name__ == "__main__":
    user_interaction()
