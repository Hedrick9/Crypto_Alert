import pandas as pd
import sqlalchemy
import psycopg2
from API_query import get_coin_price
from datetime import datetime

# GET HEADERS FROM DATABASE -> SEND HEADER LIST TO get_coin_price FUNCTION
def get_ticker_data():
    conn = psycopg2.connect('dbname=crypto_alert user=hedrick host=localhost')
    curs = conn.cursor()
    
    # get column headers AKA tickers in database
    curs.execute('''SELECT column_name FROM information_schema.columns WHERE table_name = 'tickers' ''')
    tickerList = []
    headers = []
    for item in curs.fetchall():
        tickerList.append(item[0].upper())
        headers.append(item[0])
    del tickerList [0:2]
    del headers [0:1]
    
    priceList = get_coin_price(tickerList)
    for i in range(len(priceList)):
        priceList[i] = round(priceList[i], 3)
    
    conn.close()
    return headers, priceList

# DEFINE connect FUNCTION FOR SQLALCHEMY SERVER
def connect(user, password, db, host='localhost', port=5432):
    url = 'postgresql://{}:{}@{}:{}/{}'.format(user, password, host, port, db)
    engine = sqlalchemy.create_engine(url, client_encoding='utf-8')

    return engine

# UPDATE Crypto_Alert DATABASE WITH DATA FROM get_ticker_data FUNCTION
def update_db(get_ticker_data, engine):
    
    headers, values = get_ticker_data
    time = datetime.now().strftime("%Y-%m-%d %T")
    values.insert(0, '{}'.format(time))

    new_row_dict = {}
    for i in range(len(headers)):
        new_row_dict[headers[i]] = values[i]

    new_row_df = pd.DataFrame([new_row_dict])

    new_row_df.to_sql(
                    name='tickers',
                    con=engine,
                    index=False,
                    if_exists='append'
                    )

# READ ALL DATA FROM tickers TABLE TO PANDAS DATAFRAME
def read_db(table_name, engine):
    df = pd.read_sql_table(table_name, engine)
    df.set_index('id')
    return df


#if ticker not in coinList:
#    conn = psycopg2.connect('dbname=crypto_alert user=hedrick host=localhost')
#    curs = conn.cursor()
#    curs.execute('''ALTER TABLE tickers ADD COLUMN {} DECIMAL(6,2)'''.format(ticker))
#    conn.close()
   
if __name__ == "__main__":
    engine = connect('hedrick', '', 'crypto_alert')
    update_db(get_ticker_data(), engine)
