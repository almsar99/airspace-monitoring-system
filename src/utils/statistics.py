from models.aeroplane import Aeroplane


def get_average_altitude(
    aeroplanes: list[Aeroplane],
) -> float:
    """
    Средняя высота самолетов.

    :param aeroplanes: list
    :return: float
    """
    if not aeroplanes:
        return 0.0

    total = sum(aeroplane.altitude for aeroplane in aeroplanes)

    return total / len(aeroplanes)


def get_average_velocity(
    aeroplanes: list[Aeroplane],
) -> float:
    """
    Средняя скорость самолетов.

    :param aeroplanes: list
    :return: float
    """
    if not aeroplanes:
        return 0.0

    total = sum(aeroplane.velocity for aeroplane in aeroplanes)

    return total / len(aeroplanes)


def get_max_altitude(
    aeroplanes: list[Aeroplane],
) -> float:
    """
    Максимальная высота.

    :param aeroplanes: list
    :return: float
    """
    if not aeroplanes:
        return 0.0

    return max(aeroplane.altitude for aeroplane in aeroplanes)
