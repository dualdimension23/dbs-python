from typing import Iterable, Dict, Union, List

import requests

WALLET_KEYS = ["ID", "NAME", "DESCRIPTION", "PRICE"]
ORDER_KEYS = ["ID", "TYPE", "STATUS", "BASE", "QUOTE", "TIMESTAMP", "USER_ID", "PRICE", "AMOUNT"]
ASSET_KEYS = ["ID", "PRICE", "NAME", "SYMBOL", "TYPE", "EXCHANGE", "EXCHANGE_SHORT_NAME"]


def to_json(keys, list_of_tuples):
    """
    This function will accept keys and list_of_tuples as args and return list of dicts
    """
    if not isinstance(list_of_tuples, list):
        list_of_tuples = [list_of_tuples]
    list_of_dict = [dict(zip(keys, values)) for values in list_of_tuples]
    return list_of_dict


def asset_id_to_symbol(assets, list_of_dict):
    for asset in list_of_dict:
        base_asset = asset["BASE"]
        quote_asset = asset["QUOTE"]
        print(asset)
        pure_base_asset = [tup for tup in assets if tup[0] == int(base_asset)]
        pure_quote_asset = [tup for tup in assets if tup[0] == int(quote_asset)]
        if len(pure_base_asset):
            pure_base_asset = pure_base_asset[0]
        if len(pure_quote_asset):
            pure_quote_asset = pure_quote_asset[0]
        base_symbol = pure_base_asset[3]
        quote_symbol = pure_quote_asset[3]
        asset["BASE"] = base_symbol
        asset["QUOTE"] = quote_symbol
    return list_of_dict




def get_field_name(field: str):
    return field.replace("'", "").lower()


def get_fields_repr(iterable: Iterable, is_value: bool = False):
    prefix = ":" if is_value else ""
    if isinstance(iterable, dict):
        return str(tuple(sorted(prefix + field for field in iterable if field))).replace("'", "").lower()
    elif isinstance(iterable, list):
        return str(tuple(sorted(prefix + field[0] for field in iterable if field[0].lower() != "id"))).replace("'", "").lower()
    else:
        raise RuntimeError(f"Iterable of type {type(iterable)} found! Only dict and list supported!")


def get_json_data(url: str) -> Union[Dict, List]:
    response = requests.get(url=url)
    data = response.json()
    return data
