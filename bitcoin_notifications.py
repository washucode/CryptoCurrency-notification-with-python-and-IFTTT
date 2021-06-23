import requests
import time
from datetime import datetime

BITCOIN_PRICE_THRESHOLD= 10000
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

def main():

    pass   

if __name__ == '__main__':
    main()