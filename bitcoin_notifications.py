import requests
import time
from datetime import datetime

BITCOIN_PRICE_THRESHOLD= 33700
BITCOIN_API_URL = 'https://api.coinlore.net/api/tickers/'
IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/{}/with/key/uWWPIMHdI8GgL7Ysisimk'
def get_latest_bitcoin_price():
    response = requests.get(BITCOIN_API_URL)
    json_response = response.json()
    return float(json_response['data'][0]['price_usd'])

def post_iftt_webhook(event,value):
    #The payload to be sent to IFTTT service
    data = {'value1':value}
    ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event)
    requests.post(ifttt_event_url,json=data)

# to format the way the lsit appear
def format_bitcoin_history(bitcoin_history):
        rows =[]
        for bitcoin_price in bitcoin_history:
            date= bitcoin_price['date'].strftime('%d.%m.%Y %H:%M ')
            price = bitcoin_price['price']
            row ='{}: $<b>{}</b>'.format(date,price)
            rows.append(row)

        return '<br>'.join(rows)

def main():
    
    bitcoin_history= []
    
    while True:
        price = get_latest_bitcoin_price()
        date = datetime.now()
        bitcoin_history.append({'date':date,'price':price})
        if price < BITCOIN_PRICE_THRESHOLD:
            post_iftt_webhook('bitcoin_price_emergency',price)
        # when the bitcoin_history list gets to 4
        if len(bitcoin_history)==5:
            post_iftt_webhook("bitcoin_price_update",format_bitcoin_history(bitcoin_history))

            bitcoin_history=[]
        # wait for 5 minutes befor next update.
        time.sleep(5*60)


if __name__ == '__main__':
    main()