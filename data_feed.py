from dotenv import load_dotenv
import os, pandas as pd
from oandapyV20 import API
import oandapyV20.endpoints.instruments as ins

load_dotenv()
API_ = API(os.getenv("OANDA_TOKEN"),
           environment=os.getenv("ENVIRONMENT"))

def get_prices(pair:str, count=500, gran="M1"):
    r = ins.InstrumentsCandles(instrument=pair,
                               params={"count":count,
                                       "granularity":gran,
                                       "price":"M"})
    raw = API_.request(r)["candles"]
    df  = pd.DataFrame([{"t":c["time"],
                         "c":float(c["mid"]["c"])}   # close only
                        for c in raw if c["complete"]])
    return df
