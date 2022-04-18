from typing import TypedDict


class Wallet(TypedDict):
    name: str
    description: str
    balance: float


class TraditionalAsset(TypedDict):
    symbol: str
    name: str
    price: float
    exchange: str
    exchange_short_name: str


class Order(TypedDict):
    type: str
    status: str
    user_id: int
    base: str
    quote: str
    timestamp: str
    price: float
    amount: float
