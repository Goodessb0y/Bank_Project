import json

from src.utils import transactions_data


def test_valid_list(tmp_path):
    test_file = tmp_path / "test.json"

    data = [{"id": 1}, {"id": 2}]

    with open(test_file, "w", encoding="utf-8") as f:
        json.dump(data, f)

    assert transactions_data(test_file) == data


def test_file_not_found():
    assert transactions_data("missing_file.json") == []


def test_empty_file(tmp_path):
    test_file = tmp_path / "empty.json"

    test_file.touch()

    assert transactions_data(test_file) == []


def test_invalid_json(tmp_path):
    test_file = tmp_path / "invalid.json"

    with open(test_file, "w", encoding="utf-8") as f:
        f.write("{invalid json")

    assert transactions_data(test_file) == []


def test_json_not_list(tmp_path):
    test_file = tmp_path / "dict.json"

    data = {"id": 1}

    with open(test_file, "w", encoding="utf-8") as f:
        json.dump(data, f)

    assert transactions_data(test_file) == []
