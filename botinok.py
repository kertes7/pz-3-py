# task 1
user_input = input("Введіть число: ")
try:
    number = float(user_input)
    result = number + 10
    print("Результат (рядком):", str(result))
except ValueError:
    print("Помилка: введене значення не є числом.")

# task 2

a = input("Введіть перше число: ")
b = input("Введіть друге число: ")

try:
    a = float(a)
    b = float(b)
    print(f"Сума: {a + b}")
    print(f"Різниця: {a - b}")
    print(f"Добуток: {a * b}")
    print(f"Частка: {a / b if b != 0 else 'Ділення на нуль!'}")
except ValueError:
    print("Помилка: обидва значення повинні бути числами.")


#task 3

data = input("Введіть числа через кому: ")  
try:
    number_list = [float(i.strip()) for i in data.split(",")]
    print("Список чисел:", number_list)
    print("Сума чисел:", sum(number_list))
except ValueError:
    print("Помилка: введення має містити лише числа.")

#task 4

num = input("Введіть число з плаваючою комою: ")
try:
    f_num = float(num)
    print(f"Відформатоване значення: {f_num:.2f}")
except ValueError:
    print("Помилка: введене значення не є числом.")


