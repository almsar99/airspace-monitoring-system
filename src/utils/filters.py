from models.aeroplane import Aeroplane


def filter_by_country(
    aeroplanes: list[Aeroplane],
    countries: list[str],
) -> list[Aeroplane]:
    """
    Фильтрация самолетов
    по стране регистрации.
    """
    return [aeroplane for aeroplane in aeroplanes if aeroplane.country in countries]


def sort_by_altitude(
    aeroplanes: list[Aeroplane],
) -> list[Aeroplane]:
    """
    Сортировка самолетов по высоте.
    """
    return sorted(
        aeroplanes,
        key=lambda aeroplane: aeroplane.altitude,
        reverse=True,
    )


def get_top_aeroplanes(
    aeroplanes: list[Aeroplane],
    top_n: int,
) -> list[Aeroplane]:
    """
    Получение топ N самолетов.
    """
    return aeroplanes[:top_n]
