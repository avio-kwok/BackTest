#for backtest
import pandas, talib
import requests

#download csv from web
csv_url = 'https://www.cryptodatadownload.com/cdd/FTX_BTCUSD_minute.csv'
req= requests.get(csv_url)
url_content= req.content
csv_file= open('his_data','wb')
print(csv_url)
csv_file.write(url_content)
csv_file.close

# import historical data
hp = pandas.read_csv('his_data')
#print(hp.head())

# analyis data
hp['MACD'], hp['MACDsignal'], hp['MACDhist'] = talib.MACD(hp['close'], fastperiod=12, slowperiod=26, signalperiod=9)
#print(hp.tail(50))

# stargety
# MACDsignal and MACDhist lower than 0 and MACD turn positive buy
# MACDsignal and MACDhist higher than 0 and MACD turn negitive buy
#0 for sell, 1 for buy
data=pandas.DataFrame(columns=['unix', 'price', 'buy/sell'])
#flag 0 for short,1 for long, -1 for initial
flag = -1
x=1
#bug for this algo cannot buy or sell imediately after a trade need to wait for a munite
for i in range(len(hp)):
    if flag == -1:
        if hp['MACD'][i] < 0 and hp['MACDsignal'][i] < 0 and  hp['MACDhist'][i] > 0:
            data= data.append({'unix':hp['unix'][i],
                        'price': hp['close'][i],
                        'buy/sell':'1'}, ignore_index=True)
            flag=1
            x=x+1
        elif hp['MACD'][i] > 0 and hp['MACDsignal'][i] > 0 and  hp['MACDhist'][i] < 0:
            data= data.append({'unix':hp['unix'][i],
                        'price': hp['close'][i],
                        'buy/sell':'0'}, ignore_index=True)
            flag=0
            x=x+1
    if flag == 1:
        if hp['MACDhist'][i] <= 0:
            data= data.append({'unix':hp['unix'][i],
                        'price': hp['close'][i],
                        'buy/sell':'0'}, ignore_index=True)
            flag=-1
            x=x+1
    if flag == 0:
        if hp['MACDhist'][i] >= 0:
            data= data.append({'unix':hp['unix'][i],
                        'price': hp['close'][i],
                        'buy/sell':'1'}, ignore_index=True)
            flag=-1
            x=x+1
print(data.head())
print(data.tail())
data.to_csv('outcome')
