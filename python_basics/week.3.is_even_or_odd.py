number = int(input("Введіть число: "))

# your code goes here
def is_even_or_odd(number):
    if number % 2 == 0:
        return f"число {number} парне"
    else:
        return f"число {number} непарне"
print(is_even_or_odd(number))
