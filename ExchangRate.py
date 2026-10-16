# exchangeRates = "BankOfCanadaExchangeRate.2026.csv"
# f = open(exchangeRates, "r")
# data = f.read()

# csv_data = data.splitlines()

# currency_list = csv_data[0].split(',')
# latest_exchange_rate = csv_data[-1].split(',')

# usdcad_index = currency_list.index("FXAUSDCAD")

# usd_to_cad = float(latest_exchange_rate[usdcad_index])

# cad_to_usd = 1.0 / usd_to_cad


class ExchangeRates:
    def __init__(self, exchange_rate_file):

        f = open(exchange_rate_file, "r")
        csv_data = f.read().splitlines()

        currency_list = csv_data[0].split(',')
        latest_exchange_rate = csv_data[-1].split(',')
        usdcad_index = currency_list.index("FXAUSDCAD")

        self.usd_to_cad = float(latest_exchange_rate[usdcad_index])
        self.cad_to_usd = 1.0 / self.usd_to_cad

    def convert(self, amount, from_currency, to_currency):
        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.usd_to_cad
        elif from_currency == "CAD" and to_currency == "USD":
            return amount * self.cad_to_usd

rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")

amount = float(input("Enter the amount to convert: "))
amount = round(amount, 2)
from_currency = input("Enter the currency to convert from (USD or CAD): ")
to_currency = input("Enter the currency to convert to (USD or CAD): ")

result = rates.convert(amount, from_currency, to_currency)
result = round(result, 2)

print("$" + str(amount) + " " + from_currency + " is equal to $" + str(result) + " " + to_currency)