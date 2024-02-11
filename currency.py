import requests
from datetime import date, timedelta


def currency_today(fromCurrency, amount=100, shownCurrencies=[]):
    return exchange(fromCurrency, "latest", amount, shownCurrencies)


def currency_previous(fromCurrency,daysAgo, amount=100, shownCurrencies=[]):
    last_week = date.today() - timedelta(days=daysAgo)
    return exchange(fromCurrency, last_week.strftime('%Y-%m-%d'), amount, shownCurrencies)


def exchange(fromCurrency, cur_date, amount, shownCurrencies=[]):
    # making the request to the API
    try:
        url = f"https://api.frankfurter.app/{cur_date}?amount={amount}&base={fromCurrency}"
        response = requests.get(url).json()
    except:
        return {"error": "An error occurred while trying to get the exchange rates"}

    if shownCurrencies:
        # filtering out the rest of the currencies
        filtered_rates = {}

        for k, v in response['rates'].items():
            if k in shownCurrencies:
                filtered_rates[k] = v
        response['rates'] = filtered_rates

    return response
