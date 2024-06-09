import schedule
import time
import requests

def test():
    print("Hello Geeks")
    print(time.ctime())

def get_btc_price():
    print("=====BTC=====")
    url = "https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    responce = requests.get(url=url).json()
    price = responce.get('price')
    print(f"Стоимость биткоина на текущее время: {time.ctime()}, цена {price}SOM")

 
# schedule.every(2).seconds.do(test)
# schedule.every(1).minutes.do(test)
# schedule.every().day.at("17:31").do(test)
# schedule.every().thursday.at("17:35").do(test)
schedule.every(2).seconds.do(get_btc_price)


while True:
    schedule.run_pending()
