import os
import re
import json
from modules.configloader import ConfigLoader
from util import utils
from typenv import Env

env = Env()
env.read_env()
env.prefix.append("FMP_")


class StockData:
    data_path = ConfigLoader.get_data_path("stockdata")

    @classmethod
    def load(cls):
        if os.path.exists(cls.data_path):
            print("Stock data found locally.")
            stocks = json.load(open('data/stocks.json'))
        else:
            stocks = utils.get_json_data(
                f"https://financialmodelingprep.com/api/v3/stock/list?apikey={env.str('API_KEY')}")
            print("Fetching data from remote.")
            with open("data/stocks.json", "w") as f:
                json.dump(stocks, f)

        return [{re.sub(r'(?<!^)(?=[A-Z])', '_', key).lower(): value for key, value in stock.items()} for stock in stocks]

