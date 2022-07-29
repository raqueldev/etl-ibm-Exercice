import json

import requests
import pandas as pd

URL = "https://api.apilayer.com/exchangerates_data/latest?base=EUR&apikey="

if __name__ == '__main__':
    exchanges_rates = requests.get(URL).json()
    data = pd.DataFrame(exchanges_rates)
    data[['rates']].to_csv('exchange_rates_1.csv')