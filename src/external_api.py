import os
import requests

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

url = "https://api.apilayer.com/exchangerates_data/convert"

def convert_currency(from_currency: str, to_currency: str,amount: float) -> float:

    headers = {
        "apikey": api_key
    }

    params = {
        "from":from_currency,
        "to":to_currency,
        "amount":amount
    }

    response = requests.get(url, headers=headers, params=params)
    result = response.json()

    if response.status_code != 200 or result["success"] is False:
         raise Exception(response.text)

    return float(result["result"])


def currency_amount(transaction: dict) -> float:
    currency = transaction["operationAmount"]["currency"]["code"]
    amount = float(transaction["operationAmount"]["amount"])

    if currency == "RUB":
        return amount
    elif currency == "USD" or currency == "EUR":
        converted = convert_currency(currency, "RUB", amount)
        return converted
    else:
        raise ValueError("Unknown currency code")


