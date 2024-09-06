import requests
import json

def get_exchange_rate(url):
    response=requests.get(url)
    rate=json.loads(response.content).get("rate")
    return rate

def print_now_rate(rate):
    print(f"Coin is {rate} stardusts now.")
    print(f"You have to pay {int(rate*(1/100))} stardusts for fee.")

url="https://solved.ac/api/v3/coins/exchange_rate"
exchange_rate=get_exchange_rate(url)
print_now_rate(exchange_rate)