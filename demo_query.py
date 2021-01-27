from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

tickers = ['BTC', 'ETH', 'LINK', 'ADA']
def get_coin_price(tickers):
    tickerString = ",".join(tickers)
    #ticker = ticker.upper()
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters= {
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
      grain_fed = json.dumps(data, indent=2)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
    
    #coinPrice = []
    #for item in tickers:
    #    coinPrice.append(float(data["data"][item]["quote"]["USD"]["price"]))

    return grain_fed

print(get_coin_price(tickers))
