# 1
# celsius to fahrenheit and vice versa
def convert_cel_to_far(cel):
    print("Enter a temperature in Celsius:")
    return round(cel * 9 / 5 + 32, 2)

def convert_far_to_cel(far):
    print("Enter a temperature in Fahrenheit:")
    return round((far - 32) * 5 / 9, 2)


print(convert_cel_to_far(37))
print(convert_far_to_cel(72))
