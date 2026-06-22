import json
from pathlib import Path


def transactions_data(file_path):
    file_path = Path(file_path)
    if not file_path.is_file() or file_path.stat().st_size == 0:
        return []
    else:
        with open(
            file_path,
            "r",
            encoding="utf-8",
        ) as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                return []
            if isinstance(data, list):
                return data
            return []
