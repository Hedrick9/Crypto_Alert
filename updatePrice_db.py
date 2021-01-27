import psycopg2
from API_query import get_coin_price

coinList = []

def update_db(coinList):
    conn = psycopg2.connect('dbname=crypto_alert user=hedrick host=localhost')
    curs = conn.cursor()
    
    # get column headers AKA tickers in database
    curs.execute('''SELECT column_name FROM information_schema.columns WHERE table_name = 'tickers' ''')
    tickerList = []
    for item in curs.fetchall():
        tickerList.append(item[0].upper())
    del tickerList[0:2]
    
    priceList = get_coin_price(tickerList)
    #curs.execute('''INSERT INTO tickers (time, btc, eth, link, ada) VALUES(
    
    conn.close()
    return tickerList, priceList


#if ticker not in coinList:
#    conn = psycopg2.connect('dbname=crypto_alert user=hedrick host=localhost')
#    curs = conn.cursor()
#    curs.execute('''ALTER TABLE tickers ADD COLUMN {} DECIMAL(6,2)'''.format(ticker))
#    conn.close()
   
print(update_db([1]))    
