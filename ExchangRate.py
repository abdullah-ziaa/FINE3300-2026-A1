exchangeRates = "BankOfCanadaExchangeRate.2026.csv"
f = open(exchangeRates, "r")
data = f.read()

csv_data = data.splitlines()

currency_list = csv_data[0].split(',')
latest_exchange_rate = csv_data[9].split(',')

usdcad_index = 0

for i in range(len(currency_list)):
    if currency_list[i] == "FXAUSDCAD":
        break
    else:
        usdcad_index += 1

usd_to_cad = float(latest_exchange_rate[usdcad_index])

cad_to_usd = 1 / float(usd_to_cad)