import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
SBIN = yf.Ticker("SBIN.NS").history(period='1mo',interval='15m')
SBIN=pd.DataFrame(SBIN)
SBIN["direction"]=SBIN["Close"] - SBIN["Open"]
SBIN = SBIN.dropna()
SBIN = SBIN.round({"Close": 0})
SBIN = SBIN.pivot_table(index=[SBIN["Close"]])
SBIN["True_volume"] = SBIN["Volume"]*SBIN["direction"]
SBIN = SBIN.round({"Volume": 0})
print(SBIN)
plt.scatter(SBIN.index, SBIN["True_volume"])
plt.show()
