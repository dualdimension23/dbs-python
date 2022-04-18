from modules.oracle_db import OracleDatabase


#db = OracleDatabase()
#db.connect("oracle-lab.cs.univie.ac.at:1521/lab")

"""
some_wallet: models.Wallet = {
    "id": 2,
    "name": "Petr",
    "description": "Kleiner Beidl",
    "balance": 3213.1,
}

"""

from fetch.traditional_assets import TraditionalAssetFetcher
from fetch.orders import OrderGenerator

orders = OrderGenerator().generate_orders(10)
#assets = TraditionalAssetFetcher().get_traditional_assets(2000)
#db.insert_into(values=assets, table="asset")
#print(db.select_all_from("asset"))
