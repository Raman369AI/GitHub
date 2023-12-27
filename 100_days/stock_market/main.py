import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from pandas_profiling import ProfileReport
profile = ProfileReport(df)

def magnitude(x):
    return 1 if x > 0 else -1
while True:



    SBIN = yf.Ticker("SBIN.NS").history(period='7d', interval='1m')
    profile = ProfileReport(SBIN)
    SBIN = pd.DataFrame(SBIN)
    SBIN["direction"] = SBIN["Close"] - SBIN["Open"]
    # use apply() method to apply the defined function for each row of the selected column
    SBIN["direction"] = SBIN["direction"].apply(magnitude)
    SBIN = SBIN.dropna()
    SBIN = SBIN.round({"Close": 0})
    SBIN.groupby([SBIN["direction"], SBIN["Close"]])
    SBIN["True_volume"] = SBIN["direction"] * SBIN["Volume"]
    SBIN = SBIN.round({"Volume": 0})
    print(SBIN)
    plt.bar(SBIN["Close"], SBIN["True_volume"], color=SBIN["direction"].map({1: 'g', -1: 'r'}))
    plt.show()
