import os
import json
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")

def currency_conversion(amount, currency_from, currency_to = "RUB", API_KEY = API_KEY):
    headers = {
        "apikey": API_KEY
    }
    payload = {}
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"
    request_result = requests.get(url, headers=headers, data = payload)
    result = request_result.json()
    return result['result']

print(currency_conversion(100, "USD"))