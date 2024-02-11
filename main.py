from currency import currency_today, currency_previous
from sms import send_sms
from crypto import *


def main():
    # choosing my desired currencies
    desired_currencies = ['GBP', 'EUR', 'USD', 'SEK']
    my_currency = "NOK"
    amount = 10

    # getting the exchange rates
    today = currency_today(my_currency, amount, desired_currencies)
    last_week = currency_previous(my_currency, 7, amount, desired_currencies)

    # formatting the message
    output = (f"Dagens valutakurs: \n"
              f"{today['amount']:.0f} NOK: \n"
              f"{today['date']} vs {last_week['date']} \n")

    # getting values and calculating the difference
    for k in today['rates']:
        rate_today = today['rates'][k]
        rate_last_week = last_week['rates'][k]
        difference = rate_last_week / rate_today - 1
        output += f"{k}: {rate_today:.3f} - {rate_last_week:.3f} ({difference:.2%})\n"

    # send_sms(output)


# run script
if __name__ == '__main__':
    main()
