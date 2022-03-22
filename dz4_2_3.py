import requests
import decimal


def currency_rates(currency_code):
    decimal.getcontext().prec = 4
    currency_code = currency_code.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if response.ok:
        idx = response.text.find('Date')
        date = response.text[idx+6:idx+16]
        cur = response.text.split(currency_code)
        if len(cur) == 1:
            return None
        value = decimal.Decimal((cur[1].split("</Value>")[0].split("<Value>")[1]).replace(",", "."))
        return(f"На {date} курс {currency_code}={value}")
    else:
        return None


if __name__ == "__main__":
    print(currency_rates('USD'))
    print(currency_rates('Eur'))
