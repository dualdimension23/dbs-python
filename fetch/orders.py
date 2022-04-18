import datetime
import time
import random
from modules.oracle_db import OracleDatabase
from models import models
from util import utils


class OrderGenerator:
    def __init__(self):
        self.db = OracleDatabase()
        self.db.connect("oracle-lab.cs.univie.ac.at:1521/lab")
        self._assets = []

    def generate_orders(self, n: int):
        self._assets = self.db.select_all_from("asset")
        orders = [models.Order(**self._generate_order()) for _ in range(n)]
        self.db.insert_into(values=orders, table="orders")
        return orders

    def _generate_order(self):
        order_type = random.choice(["bid", "ask"])
        status = random.choice(["unfilled"])
        base_asset = random.choice(self._assets)
        quote_asset = random.choice(self._assets)
        while not base_asset[1] or not quote_asset[1]:
            base_asset = random.choice(self._assets)
            quote_asset = random.choice(self._assets)
        base_id = base_asset[0]
        quote_id = quote_asset[0]
        price = quote_asset[1] / base_asset[1]
        timestamp = datetime.datetime.now()
        timestamp = time.mktime(timestamp.timetuple())
        amount = random.uniform(0, 20)
        return dict(
            type=order_type,
            status=status,
            base=base_id,
            quote=quote_id,
            price=price,
            user_id=random.randint(0, 1000),
            timestamp=timestamp,
            amount=amount
        )
