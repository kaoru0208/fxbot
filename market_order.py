import json
import os

import oandapyV20.endpoints.orders as orders
from dotenv import load_dotenv
from oandapyV20 import API

load_dotenv()
api = API(access_token=os.getenv("OANDA_TOKEN"), environment=os.getenv("ENVIRONMENT"))
acc_id = os.getenv("OANDA_ACCOUNT")

data = {
    "order": {
        "instrument": "USD_JPY",
        "units": "1000",  # プラスで BUY, マイナスで SELL
        "type": "MARKET",
        "positionFill": "DEFAULT",
    }
}

r = orders.OrderCreate(accountID=acc_id, data=data)
print(json.dumps(api.request(r), indent=2))
