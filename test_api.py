import json
import os

import oandapyV20.endpoints.pricing as pricing
from dotenv import load_dotenv
from oandapyV20 import API

load_dotenv()  # .env 読み込み

api = API(
    access_token=os.getenv("OANDA_TOKEN"),
    environment=os.getenv("ENVIRONMENT"),  # practice / live
)
acc_id = os.getenv("OANDA_ACCOUNT")

r = pricing.PricingInfo(  # 価格問い合わせ
    accountID=acc_id, params={"instruments": "USD_JPY"}
)
resp = api.request(r)  # ← ここが 200 になる
print(json.dumps(resp["prices"][0], indent=2))
