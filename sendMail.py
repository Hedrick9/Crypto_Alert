from bs4 import BeautifulSoup
import requests
import time
import smtplib
from email.message import EmailMessage

# smtp module defines an SMTP client session object that can be used to send mail to any
# internet machine with an SMTP or ESMTP listener daemon.

def email_alert(subject, body, to_emails):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = ', '.join(to_emails)
    
    user = "CryptoAlert.RH@gmail.com"
    msg['from'] = user
    #password = "Young tailored gibson"
    app_password = "suwcohwwhcdbcsxl"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, app_password)
    server.send_message(msg)

    server.quit()

def update_message(coin, coin_price):
    message = "{} price: ${}".format(coin, str(coin_price))
    return message

if __name__ == '__main__':
    email_alert("Crypto Update", update_message('Ethereum', get_crypto_price('ether')), ["9135752423@txt.att.net", "hedrickrussell@gmail.com"])

