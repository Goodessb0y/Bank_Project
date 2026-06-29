import json
import logging
from pathlib import Path
from typing import Dict, Any
from config import ROOT_DIR

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"{ROOT_DIR}//logs//utils.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def transactions_data(file_path: str) -> list[dict[str, Any]]:
    path = Path(file_path)
    if not path.is_file() or path.stat().st_size == 0:
        logger.error("File not found")
        return []
    else:
        with path.open(
            "r",
            encoding="utf-8",
        ) as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    logger.info(f"list data loaded from {path}")
                    return data
            except json.decoder.JSONDecodeError:
                logger.error("json data decode error")
                return []
            logger.error("json data not list type")
            return []
