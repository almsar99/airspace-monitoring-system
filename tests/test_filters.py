from models.aeroplane import Aeroplane
from utils.filters import (
    filter_by_country,
    get_top_aeroplanes,
    sort_by_altitude,
)


def test_filter_by_country():
    aeroplanes = [
        Aeroplane("A", "Germany", 100, 1000),
        Aeroplane("B", "France", 100, 2000),
    ]

    result = filter_by_country(
        aeroplanes,
        ["Germany"],
    )

    assert len(result) == 1
    assert result[0].country == "Germany"


def test_sort_by_altitude():
    aeroplanes = [
        Aeroplane("A", "Germany", 100, 1000),
        Aeroplane("B", "France", 100, 5000),
    ]

    result = sort_by_altitude(aeroplanes)

    assert result[0].altitude == 5000


def test_get_top_aeroplanes():
    aeroplanes = [
        Aeroplane("A", "Germany", 100, 1000),
        Aeroplane("B", "France", 100, 5000),
    ]

    result = get_top_aeroplanes(
        aeroplanes,
        1,
    )

    assert len(result) == 1


def test_empty_filter():
    aeroplanes = []

    result = filter_by_country(
        aeroplanes,
        ["Germany"],
    )

    assert result == []
