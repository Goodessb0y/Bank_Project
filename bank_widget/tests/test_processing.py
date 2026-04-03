import pytest
from bank_widget.src.processing import *


@pytest.fixture
def filter_state_cases():
    data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "PENDING"},
        {"id": 3, "state": "EXECUTED"},
        {"id": 4, "state": "CANCELLED"},
    ]
    return [
        (data, "EXECUTED", [{"id": 1, "state": "EXECUTED"}, {"id": 3, "state": "EXECUTED"}]),
        (data, "PENDING", [{"id": 2, "state": "PENDING"}]),
        (data, "CANCELLED", [{"id": 4, "state": "CANCELLED"}]),
        (data, "UNKNOWN", []),
        ([], "EXECUTED", []),
    ]


@pytest.mark.parametrize("index", range(5))
def test_filter_by_state(filter_state_cases, index):
    account_number, state, expected = filter_state_cases[index]
    assert filter_by_state(account_number, state) == expected


@pytest.fixture
def sort_date_cases():
    data = [
        {"id": 1, "date": "2024-06-01"},
        {"id": 2, "date": "2024-06-03"},
        {"id": 3, "date": "2024-06-02"},
        {"id": 4, "date": "2024-06-02"},
    ]
    return [
        (
            data,
            True,
            [
                {"id": 2, "date": "2024-06-03"},
                {"id": 3, "date": "2024-06-02"},
                {"id": 4, "date": "2024-06-02"},
                {"id": 1, "date": "2024-06-01"},
            ],
        ),
        (
            data,
            False,
            [
                {"id": 1, "date": "2024-06-01"},
                {"id": 3, "date": "2024-06-02"},
                {"id": 4, "date": "2024-06-02"},
                {"id": 2, "date": "2024-06-03"},
            ],
        ),
        ([], True, []),
        ([{"id": 5, "date": "20240606"}], True, [{"id": 5, "date": "20240606"}]),
    ]


@pytest.mark.parametrize("index", range(4))
def test_sort_by_date(sort_date_cases, index):
    data, sort, expected = sort_date_cases[index]
    assert sort_by_date(data, sort) == expected
