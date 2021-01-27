from API_query import get_coin_price
from inbox import get_inbox
import sendMail
import time

users = {"Mark_email": "mduesler26@gmail.com", "Mark_phone": "9495841177@text.att.net"}

while True:
    #ticker = input("Enter the ticker for the coin price you would like to track:\n")
    
    check_inbox = get_inbox()
    if len(check_inbox) > 0:
        print(check_inbox)
        print('Inbox length: {}\n'.format(len(check_inbox)))
    else:
        print("No new messages\n")
    for item in check_inbox:
        message, *_ = item['body'].split('\r')
        print(len(message))
        user = item['from'].split()
        print(len(user))
        print(user)

    try:
        coinList = []
        coinList.append(message)
        coinPrice = get_coin_price(coinList)
        
        print(coinPrice)
    except Exception:
        print('Sorry. The ticker you supplied does not exist!')
        pass

    time.sleep(60)
