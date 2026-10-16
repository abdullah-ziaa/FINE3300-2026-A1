# Create a class called ExchangeRates that reads the exchange rate data from a CSV file and provides a method to convert between USD and CAD.
class ExchangeRates:
    # Initialize the ExchangeRates class with the exchange rate data from a CSV file.
    def __init__(self, exchange_rate_file):

        # Read the exchange rate data from the CSV file and store all of the data in a list.
        file = open(exchange_rate_file, "r")
        csv_data = file.read().splitlines()

        # Split the first line of the CSV data to get the list of currencies and the last line to get the latest exchange rates.
        currency_list = csv_data[0].split(',')
        latest_exchange_rate = csv_data[-1].split(',')

        # Find the index of the USD to CAD rates column in the currency list and use it to get corresponding latest exchange rate.
        usdcad_index = currency_list.index("FXAUSDCAD")
        self.usd_to_cad = float(latest_exchange_rate[usdcad_index])
        self.cad_to_usd = 1.0 / self.usd_to_cad

    # Create a method called convert that uses an inputted amount, from_currency, and to_currency to convert between USD and CAD using the calculated latest exchange rates.
    def convert(self, amount, from_currency, to_currency):
        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.usd_to_cad
        elif from_currency == "CAD" and to_currency == "USD":
            return amount * self.cad_to_usd

# Create an instance of the ExchangeRates class and use it to gather the appropriate converstion rates based on the given CSV file.
rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")

# Prompt the user for an amount, from_currency, and to_currency to convert between USD and CAD in accordance with the desired outcome.
amount = float(input("Enter the amount to convert: "))
amount = round(amount, 2)
from_currency = input("Enter the currency to convert from (USD or CAD): ")
to_currency = input("Enter the currency to convert to (USD or CAD): ")

# Calculcate the conversion result using the convert method in the ExchangeRates class, ensuring to round to two decimal places.
result = rates.convert(amount, from_currency, to_currency)
result = round(result, 2)

# Print the result  of the conversion in an easy to understand format for the user.
print("$" + str(amount) + " " + from_currency + " is equal to $" + str(result) + " " + to_currency + ".")