from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def get_coin_price(tickers):
    tickerString = ",".join(tickers)
    
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
      'symbol': tickerString
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': "ef3f9e12-4b59-48a1-b2f0-d772d463ac54" 
    }
    
    session = Session()
    session.headers.update(headers)
    
    try:
      response = session.get(url, params=parameters)
      data = response.json()
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
    
    coinList = []
    for item in tickers:
        coinPrice = float(data["data"][item]["quote"]["USD"]["price"])
        coinList.append(coinPrice)

    return coinList

#tickerL = ['ETH', 'BTC', 'LINK', 'ADA', 'OX', 'YFI', 'ALGO']
#print(get_coin_price(['ETH']))
