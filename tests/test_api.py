from unittest.mock import MagicMock, patch

import pytest

from api.aeroplanes_api import AeroplanesAPI


@patch("api.aeroplanes_api.requests.Session")
def test_get_country_coordinates(mock_session):
    mock_response = MagicMock()

    mock_response.status_code = 200

    mock_response.json.return_value = [
        {
            "boundingbox": [
                "1",
                "2",
                "3",
                "4",
            ]
        }
    ]

    mock_session.return_value.get.return_value = mock_response

    api = AeroplanesAPI()

    result = api._AeroplanesAPI__get_country_coordinates("Germany")

    assert result == ["1", "2", "3", "4"]


@patch("api.aeroplanes_api.requests.Session")
def test_get_data(mock_session):
    first_response = MagicMock()
    first_response.status_code = 200

    first_response.json.return_value = [
        {
            "boundingbox": [
                "1",
                "2",
                "3",
                "4",
            ]
        }
    ]

    second_response = MagicMock()
    second_response.status_code = 200

    second_response.json.return_value = {"states": [["plane"]]}

    mock_session.return_value.get.side_effect = [
        first_response,
        second_response,
    ]

    api = AeroplanesAPI()

    result = api.get_data("Germany")

    assert result == [["plane"]]


@patch("api.aeroplanes_api.requests.Session")
def test_country_not_found(mock_session):
    mock_response = MagicMock()

    mock_response.status_code = 200
    mock_response.json.return_value = []

    mock_session.return_value.get.return_value = mock_response

    api = AeroplanesAPI()

    with pytest.raises(ValueError):
        api._AeroplanesAPI__get_country_coordinates("Unknown")
