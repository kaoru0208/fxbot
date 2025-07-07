import datetime as dt
import json

from data_feed import get_prices
from order_api import market_order

FAST, SLOW = 5, 20  # periods


def run_once():
    df = get_prices("USD_JPY", 200)
    ema_f = df["c"].ewm(span=FAST).mean().iloc[-1]
    ema_s = df["c"].ewm(span=SLOW).mean().iloc[-1]

    if ema_f > ema_s:
        res = market_order(+1000)  # long 1000 units
    elif ema_f < ema_s:
        res = market_order(-1000)  # short
    else:
        res = {"info": "no trade"}

    stamp = dt.datetime.utcnow().isoformat()
    print(stamp, json.dumps(res, indent=2))
