miles = float(input("Введіть кількість миль: "))

# your code goes here
def convert_miles_to_km(miles):
    km = miles * 1.6
    return round(km, 2)
print(convert_miles_to_km(miles))

# Для набору вхідних даних (милі = 2) – функція повертає – 3.2
# Для набору вхідних даних (милі = 3.3) – функція повертає – 5.28