import asyncio
import threading

import models.models
from modules.oracle_db import OracleDatabase
import time
from util import utils

import websockets


async def send(client, message):
    await client.send(message)


async def handler(client, path):
    # Register.
    print("Websocket Client Connected.", client)
    clients.append(client)
    while True:
        try:
            print("ping", client)
            pong_waiter = await client.ping()
            await pong_waiter
            print("pong", client)
            time.sleep(3)
        except Exception as e:
            clients.remove(client)
            print("Websocket Client Disconnected", client)
            break

clients = []
start_server = websockets.serve(handler, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
threading.Thread(target=asyncio.get_event_loop().run_forever).start()

db = OracleDatabase()
db.connect("oracle-lab.cs.univie.ac.at:1521/lab")
print("Socket Server Running. Starting main loop.")
while True:
    data = db.select_all_from("orders")
    data = utils.to_json(utils.ORDER_KEYS, data)
    data = utils.asset_id_to_symbol(db.select_all_from("asset"), data)
    data = str(data).replace("'", '"')
    print(data)
    time.sleep(0.5)
    message_clients = clients.copy()
    for client in message_clients:
        print("Sending", data, "to", client)
        try:
            asyncio.run(send(client, data))
        except:
            # Clients might have disconnected during the messaging process,
            # just ignore that, they will have been removed already.
            pass