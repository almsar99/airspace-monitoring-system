from unittest.mock import patch

from main import print_aeroplanes
from models.aeroplane import Aeroplane


def test_print_aeroplanes(capsys):
    aeroplanes = [
        Aeroplane(
            "DLH123",
            "Germany",
            250,
            10000,
        )
    ]

    print_aeroplanes(aeroplanes)

    captured = capsys.readouterr()

    assert "DLH123" in captured.out


@patch("builtins.input", side_effect=["Germany", "1", "Germany"])
@patch("main.print_aeroplanes")
@patch("main.JSONSaver")
@patch("main.AeroplanesAPI")
def test_user_interaction(
    mock_api,
    mock_saver,
    mock_print,
    mock_input,
):
    mock_api.return_value.get_data.return_value = [
        [
            "abcd",
            "DLH123",
            "Germany",
            None,
            None,
            None,
            None,
            None,
            None,
            250,
            None,
            None,
            None,
            10000,
        ]
    ]

    from main import user_interaction

    user_interaction()

    assert mock_api.called
