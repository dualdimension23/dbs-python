from modules.oracle_db import OracleDatabase
from models import models


db = OracleDatabase()
db.connect("oracle-lab.cs.univie.ac.at:1521/lab")

some_wallet: models.Order = {
    "amount": 2342343,
    "base": "123",
    "price": 3432423,
    "quote": "124",
    "status": "ehstatus",
    "timestamp": "23123123",
    "type": "BID",
    "user_id":  9999999

}



#db.insert_into(values=[some_wallet], table="orders")
db.execute("DELETE FROM orders WHERE type='hiibidi'")
#print(db.cursor.fetchall())

