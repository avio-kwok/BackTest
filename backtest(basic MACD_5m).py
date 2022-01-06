#for backtest
from typing_extensions import runtime
import pandas, talib
import requests

# import historical data
hp = pandas.read_csv('his_data')
print(hp.head(6))
print(hp.tail(6))
#for 5 min time frame
i=0
print(hp.loc[i])
hp_5m=pandas.DataFrame(columns=list(hp.columns))
print(hp_5m)
while i<len(hp):
    print('runing',i)
    hp_5m=hp_5m.append(hp.loc[i],ignore_index=True)
    i=i+4

print(hp_5m.head(2))
print(hp_5m.tail(2))

hp_5m.to_csv('his_data_5m')