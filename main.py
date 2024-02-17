from currency import currency_today, currency_previous
from sms import send_sms
from crypto import crypto_rate
from config import my_currency, desired_currencies, prev_currency_days, amount, desired_crypto


def main():

    # getting the exchange rates
    today = currency_today(my_currency, amount, desired_currencies)
    earlier_currency = currency_previous(my_currency, prev_currency_days, amount, desired_currencies)
    crypto = crypto_rate(desired_crypto)
  
    # getting values and calculating the difference
    try:
        currency_list = f"Valutakurs: \n{amount} NOK: \n{today['date']} vs {earlier_currency['date']} \n"   
        for k in today['rates']:
            rate_today = today['rates'][k]
            rate_earlier = earlier_currency['rates'][k]
            difference = rate_earlier / rate_today - 1
            currency_list += f"{k}: {rate_today:.3f} - {rate_earlier:.3f} ({difference:.2%})\n"
    except:
        currency_list += today

    # getting the crypto values
    try:
        crypto_list = "Dagens cryptokurs vs igår:\n"
        for k,v in crypto.items():
            today = v['price_now']
            earlier = v['price_earlier']
            change = v['price_change_percent']
            from_cur = v['from_currency']
            crypto_list += f"{k}: {today} - {earlier} {from_cur} ({change})\n"
    except:
        crypto_list += crypto
    
    # formatting the message
    output = (f"Dagens oppdatering:\n"
              f"{currency_list}\n"
              f"{crypto_list}")

    print(output)
    send_sms(output)


# run script
if __name__ == '__main__':
    main()
