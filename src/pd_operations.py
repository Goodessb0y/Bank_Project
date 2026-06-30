from pathlib import Path
from typing import Any

import pandas as pd

from config import ROOT_DIR

path = f"{ROOT_DIR}/data/transactions.csv"


def get_transactions_csv(path: str | Path) -> list[dict[str, Any]]:
    """
    Функция для считывания финансовых операций из CSV
    Вход: путь до csv-файла
    Выход: записи транзакций списком словарей
    """
    data = pd.read_csv(path)
    return data.to_dict(orient="records")


def get_transactions_excel(path: str | Path) -> list[dict[str, Any]]:
    """
    Функция для считывания финансовых операций из Excel
    Вход: путь до Excel-файла
    Выход: записи транзакций списком словарей
    """
    data = pd.read_excel(path)
    return data.to_dict(orient="records")
