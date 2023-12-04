def analyze_text(text):
    russian_letters = set("ыъёэ")

    if any(letter in russian_letters for letter in text.lower()):
        print("Ми не обслуговуємо замовлення мовою окупантів. Слава Україні!")
    else:
        print("Дякуємо за замовлення!")

user_input = input("Введіть текст: ")
analyze_text(user_input)




