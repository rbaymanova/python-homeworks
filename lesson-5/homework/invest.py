# 2
# investment calculator
def invest(amount, rate, years):
    for year in range(years):
        amount = round(amount * (1 + rate), 2)
        print(f"Year {year}: {amount}")

invest(100, .05, 4)