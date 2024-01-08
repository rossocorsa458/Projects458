#pip install forex-python

from forex_python.converter import CurrencyRates 

cr = CurrencyRates()

amount = int(input("Please enter the amount you want to convert: "))

from_currency = input("Please enter the currency code that has to be converted: ").upper()

to_currency = input("Please enter the currency code to convert: ").upper()

result = cr.convert(from_currency, to_currency, amount)

print("The converted rate of",amount,from_currency,"is",result,to_currency)