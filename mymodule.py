name = "Bob"  # Глобальная переменная модуля

def hello():  # Функция выводит приветствие с использованием переменной name
    print("Hello " + name)

hello()  # Вызов функции при загрузке модуля

def add_three_numbers(a, b, c):  # Функция суммирует три числа, если ни одно из них не равно нулю
    if a != 0 and b != 0 and c != 0:
        return "Sum: ", a + b + c
    else:
        return "Some is zero"
