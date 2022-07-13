import requests
import pandas as pd
from common import get_config

# URL = 'https://api.apilayer.com/exchangerates_data/live?base=USD&symbols=EUR&apikey=' + config["apiKey"]["api_key"]

if __name__ == '__main__':
    config = get_config()
    print config["apiKey"]["api_key"]