import random
from typing import List, Dict

from typenv import Env
from modules.stockdata import StockData
from models import models

env = Env()
env.read_env()
env.prefix.append("FMP_")


class TraditionalAssetFetcher:

    def __init__(self):
        self.traditional_assets: List = []

    def _fetch(self, number: int) -> List[Dict]:
        """
        Fetches data of traditional assets.
        :param number: Number of assets to be returned
        :return: List of traditional assets
        """
        self.traditional_assets = StockData.load()
        random.shuffle(self.traditional_assets, lambda: 0.1)
        if number < len(self.traditional_assets):
            return self.traditional_assets[:number]
        else:
            return self.traditional_assets

    def get_traditional_assets(self, number: int):
        assets = self._fetch(number)
        return [models.TraditionalAsset(**asset) for asset in assets]
