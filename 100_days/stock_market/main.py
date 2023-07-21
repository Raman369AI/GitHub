import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
def magnitude(x):
    if x>0:
        return 1
    elif x==0:
        return 0
    elif x<0:
        return -1

SBIN = yf.Ticker("SBIN.NS").history(period='7d',interval='5m')
SBIN=pd.DataFrame(SBIN)
SBIN["direction"]=SBIN["Close"] - SBIN["Open"]
#use apply() method to apply the defined function for each row of the selected column
SBIN["direction"]=SBIN["direction"].apply(magnitude)
SBIN = SBIN.dropna()
SBIN = SBIN.round({"Close": 0})
SBIN = SBIN.pivot_table(index=[SBIN["Close"]])

SBIN["True_volume"] = SBIN["direction"]
SBIN = SBIN.round({"Volume": 0})
print(SBIN)
plt.scatter(SBIN.index, SBIN["direction"])
plt.show()
