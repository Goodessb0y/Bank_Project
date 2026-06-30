from unittest.mock import patch

import pandas as pd

from src.pd_operations import get_transactions_csv, get_transactions_excel


def test_get_transactions_csv():
    df = pd.DataFrame(
        {
            "id": [1, 2, 3],
            "name": ["A", "B", "C"],
        }
    )

    with patch("pandas.read_csv", return_value=df) as mock_read:
        result = get_transactions_csv("test.csv")

    mock_read.assert_called_once_with("test.csv")

    assert result == [
        {"id": 1, "name": "A"},
        {"id": 2, "name": "B"},
        {"id": 3, "name": "C"},
    ]


def test_get_transactions_excel():
    df = pd.DataFrame(
        {
            "id": [1, 2, 3],
            "name": ["A", "B", "C"],
        }
    )

    with patch("pandas.read_excel", return_value=df) as mock_read:
        result = get_transactions_excel("test.xlsx")

    mock_read.assert_called_once_with("test.xlsx")

    assert result == [
        {"id": 1, "name": "A"},
        {"id": 2, "name": "B"},
        {"id": 3, "name": "C"},
    ]
