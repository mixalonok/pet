import requests
import json

API_key = "https://api.binance.com/api/v3/exchangeInfo"


result=requests.get(API_key).json()

with open('result.json', 'w') as json_file:
    json.dump(result, json_file)