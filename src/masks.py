import logging

from config import ROOT_DIR

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"{ROOT_DIR}//logs//masks.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

error_1 = "Неверное количество символов {0}"
error_2 = "Некорректный номер карты"


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты."""

    logger.debug("Выполняем маскировку номера карты")

    card_number = card_number.replace(" ", "")

    if len(card_number) != 16:
        logger.error(error_1.format(len(card_number)))
        raise ValueError(error_1.format(len(card_number)))

    example = "111111******1111"
    masked = []

    for index, char in enumerate(card_number):
        if not char.isdigit():
            logger.error(error_2)
            raise ValueError(error_2)

        masked.append(char if example[index] != "*" else "*")

    result = "".join(masked)
    result = " ".join(result[i : i + 4] for i in range(0, 16, 4))

    logger.info("Номер карты замаскирован")

    return result


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера аккаунта"""
    if len(account_number) < 4:
        logger.error(error_1.format(len(account_number)))
        raise ValueError(error_1.format(len(account_number)))

    logger.info("Успешно")
    return "*" * 2 + account_number[-4:]
