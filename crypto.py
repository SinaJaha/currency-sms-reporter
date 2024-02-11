import requests
import urllib.parse
from datetime import datetime


def crypto_rate(assets):
    # getting the current exchange rates for the desired assets
    assets_string = urllib.parse.quote(str(assets).replace("'", '"').replace(' ', ''))
    link = f"https://api4.binance.com/api/v3/ticker/24hr?symbols={assets_string}"


    response = requests.get(link).json()
    if 'code' in response:
        return f"Error in getting crypto!\ncode: {response['code']}\nerror: {response['msg']}"
 
    

    # Prepare a dictionary to hold the filtered rates
    filtered_rates = {}

    for item in response:
        # giving the json a better structure with the currency as the key
        currency = item['symbol'][3:6]
        name = item['symbol'][:3]
        percent_change = item['priceChangePercent']
    
        if float(percent_change) > 0:
            percent_change = f"+{round(float(percent_change), 2)}%"
        else:
            percent_change = f"{round(float(percent_change), 2)}%"
        
        filtered_rates[name] = {
            'earlier_date': f"{datetime.fromtimestamp(item['openTime']/1000).strftime('%Y-%m-%d')}",
            'earlier_time': f"{datetime.fromtimestamp(item['openTime']/1000).strftime('%H:%M')}",
            'from_currency': currency,
            'price_now': f"{round(float(item['lastPrice']), 2)}",
            'price_earlier': f"{round(float(item['openPrice']), 2)}",
            'price_change': f"{round(float(item['priceChange']), 2)}",
            'price_change_percent': percent_change
        }  
  
    
    return filtered_rates
