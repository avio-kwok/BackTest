# to calculate profit with trades
from numpy import nan
import pandas as pd

trades= pd.read_csv('trades(basic MACD)')
data=pd.DataFrame(columns=['money', 'position'])
# having 100 usd as initial value
money= 200
position= 0
data= data.append({'money':"{:.2f}".format(money),'position': "{:.2f}".format(position)},ignore_index=True)
for i in range(len(trades)):
    if position != 0:
        money= money+position*trades['price'][i]
        position= 0
    elif trades['buy/sell'][i] == 1:
        position= money*0.7/trades['price'][i]    
        money= money*0.3
    else:
        position= -(money*0.7/trades['price'][i])
        money= money*1.7
    data= data.append({'money':"{:.2f}".format(money),'position': "{:.2f}".format(position)},ignore_index=True)
    print('diu',i)

print(data.head())
print(data.tail())
data.to_csv('result(basic MACD)')
