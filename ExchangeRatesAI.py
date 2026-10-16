"""USD <-> CAD exchange rate calculator using Bank of Canada annual rates."""

import csv
from decimal import Decimal, ROUND_HALF_UP


class ExchangeRates:
    """Reads annual exchange rates from a Bank of Canada CSV file.

    The Bank of Canada reports rates as "CAD per 1 unit of foreign currency",
    so the FXAUSDCAD column is the number of Canadian dollars per 1 US dollar.
    """

    def __init__(self, filename, year=None):
        """Load the USD/CAD rate from `filename`.

        If `year` is None, the most recent year in the file is used.
        """
        self.rates = {}  # {year (int): USD->CAD rate (float)}
        # utf-8-sig strips the byte-order mark some Bank of Canada files carry
        with open(filename, newline="", encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                row_year = int(row["Date"][:4])
                self.rates[row_year] = float(row["FXAUSDCAD"])

        self.year = year if year is not None else max(self.rates)
        self.usd_to_cad = self.rates[self.year]

    def convert(self, amount, from_currency, to_currency):
        """Convert `amount` from one currency (USD or CAD) to the other.

        Returns a string rounded to the nearest penny, e.g. "$1,397.80 CAD".
        """
        from_currency = from_currency.strip().upper()
        to_currency = to_currency.strip().upper()
        amount = Decimal(str(amount))
        rate = Decimal(str(self.usd_to_cad))

        if from_currency == to_currency:
            result = amount
        elif from_currency == "USD":  # USD -> CAD
            result = amount * rate
        else:  # CAD -> USD
            result = amount / rate

        result = result.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        return f"${result:,.2f} {to_currency}"


def main():
    rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")

    amount = float(input("Enter the amount: "))
    from_currency = input("Convert from (USD or CAD): ")
    to_currency = input("Convert to (USD or CAD): ")

    original = f"${amount:,.2f} {from_currency.strip().upper()}"
    converted = rates.convert(amount, from_currency, to_currency)

    print(f"\nUsing the {rates.year} rate: 1 USD = {rates.usd_to_cad} CAD")
    print(f"{original} = {converted}")


if __name__ == "__main__":
    main()