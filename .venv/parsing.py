import requests
import json

def get_price_ticket(ticked_code):
    API_key = f"https://api.binance.com/api/v3/exchangeInfo?symbol={ticked_code}"
    data = requests.get(API_key).json()
    return data

result=get_price_ticket("ETHBTC")
#print(result)

with open('result.json', 'w') as json_file:
    json.dump(result, json_file)