from currency import currency_today, currency_previous
from sms import send_sms
from crypto import crypto_rate


def main():
    # choosing my desired currencies
    my_currency = "NOK"
    desired_currencies = ['GBP', 'EUR', 'USD', 'SEK']
    prev_currency_days = 1
    amount = 100
    # choosing my desired crypto
    desired_crypto = ['BTCEUR', 'ETHUSDT']
    

    # getting the exchange rates
    today = currency_today(my_currency, amount, desired_currencies)
    earlier_currency = currency_previous(my_currency, prev_currency_days, amount, desired_currencies)
    crypto = crypto_rate(desired_crypto)

    # formatting the message
    output = (f"Dagens valutakurs: \n"
              f"{amount} NOK: \n"
              f"{today['date']} vs {earlier_currency['date']} \n")

    # getting values and calculating the difference
    for k in today['rates']:
        rate_today = today['rates'][k]
        rate_earlier = earlier_currency['rates'][k]
        difference = rate_earlier / rate_today - 1
        output += f"{k}: {rate_today:.3f} - {rate_earlier:.3f} ({difference:.2%})\n"

    output += "\n\nDagens cryptokurs vs igår:\n"

    for k,v in crypto.items():
        today = v['price_now']
        earlier = v['price_earlier']
        change = v['price_change_percent']
        from_cur = v['from_currency']
        output += f"{k}: {today} - {earlier} {from_cur} ({change})\n"

    print(output)
    send_sms(output)


# run script
if __name__ == '__main__':
    main()
