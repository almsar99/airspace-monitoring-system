from api.aeroplanes_api import AeroplanesAPI
from models.aeroplane import Aeroplane
from storage.json_saver import JSONSaver
from utils.filters import (
    filter_by_country,
    get_top_aeroplanes,
    sort_by_altitude,
)


def print_aeroplanes(aeroplanes: list[Aeroplane]) -> None:
    """
    Вывод самолетов в консоль.

    :param aeroplanes: Список самолетов
    """
    for aeroplane in aeroplanes:
        print(aeroplane)


def user_interaction() -> None:
    """Функция взаимодействия с пользователем."""
    country = input("Введите название страны: ")

    api = AeroplanesAPI()

    try:
        raw_data = api.get_data(country)
    except Exception as error:
        print(f"Ошибка: {error}")
        return

    aeroplanes = Aeroplane.cast_to_object_list(raw_data)

    saver = JSONSaver()

    for aeroplane in aeroplanes:
        saver.add(aeroplane)

    print(f"\nНайдено самолетов: {len(aeroplanes)}")

    top_n = int(input("\nВведите количество самолетов для топа: "))

    sorted_aeroplanes = sort_by_altitude(aeroplanes)

    top_aeroplanes = get_top_aeroplanes(
        sorted_aeroplanes,
        top_n,
    )

    print("\nТоп самолетов по высоте:\n")

    print_aeroplanes(top_aeroplanes)

    countries_input = input("\nВведите страны регистрации через запятую: ")

    countries = countries_input.split(",")

    countries = [country.strip() for country in countries]

    filtered_aeroplanes = filter_by_country(
        aeroplanes,
        countries,
    )

    print("\nСамолеты по стране регистрации:\n")

    print_aeroplanes(filtered_aeroplanes)


if __name__ == "__main__":
    user_interaction()
