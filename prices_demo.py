from dotenv import load_dotenv
import os, json
from oandapyV20 import API
import oandapyV20.endpoints.pricing as pricing

load_dotenv()
api = API(access_token=os.getenv("OANDA_TOKEN"),
          environment=os.getenv("ENVIRONMENT"))
acc = os.getenv("OANDA_ACCOUNT")

r = pricing.PricingInfo(accountID=acc,
                        params={"instruments": "USD_JPY"})
print(json.dumps(api.request(r)["prices"][0], indent=2))
