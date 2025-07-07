import os

import oandapyV20.endpoints.orders as orders
from dotenv import load_dotenv
from oandapyV20 import API

load_dotenv()
ACC = os.getenv("OANDA_ACCOUNT")
api = API(os.getenv("OANDA_TOKEN"), environment=os.getenv("ENVIRONMENT"))


def market_order(units: int, pair: str = "USD_JPY"):
    data = {
        "order": {
            "units": str(units),
            "instrument": pair,
            "type": "MARKET",
            "positionFill": "DEFAULT",
        }
    }
    r = orders.OrderCreate(ACC, data=data)
    return api.request(r)
