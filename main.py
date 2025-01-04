import math

def calculator():
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            return "Деление на ноль невозможно!"
        return x / y

    while True:
        print("1:[+] | 2:[-] | 3:[*] | 4:[/]")
        choice = input("Введите номер операции (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")

            next_calculation = input("Хотите выполнить еще одну операцию? (да/нет): ")
            if next_calculation.lower() != 'да':
                break
        else:
            print("Некорректный ввод. Пожалуйста, выберите правильную операцию.")

def convert_base(number, from_base, to_base):
    decimal_number = int(number, from_base)
    digits = "0123456789ABCDEF"
    result = ""
    while decimal_number > 0:
        remainder = decimal_number % to_base
        result = digits[remainder] + result
        decimal_number = decimal_number // to_base
    return result or "0"

def sistsch():
    number = input("Введите число: ")
    from_base = int(input("Введите исходную систему счисления: "))
    to_base = int(input("Введите целевую систему счисления: "))
    result = convert_base(number, from_base, to_base)
    print(f"Число {number} из системы счисления {from_base} в систему счисления {to_base} равно {result}")

def stepeni():
    ch = int(input("Введите число: "))
    step = int(input("Введите до какой степени возводить это число: "))
    result = pow(ch, step)
    print(f"Результат: {ch} в степени {step} равно {result}")

def modul():
    ch = int(input("Введите число:  "))
    if ch < 0:
        ch = -ch
        print(f"Модуль числа {-ch} равен {ch}")
    else:
        print(f"Модуль числа {ch} равен {ch}")

def pif3():
    n = int(input("Введите число:  "))
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            c = (a * a + b * b) ** 0.5
            c_int = int(c)
            if c == c_int and c <= n:
                print(a, b, c_int)

def delit():
    cif = int(input("Введите число:  "))
    if cif == 1:
        d = 1
    else:
        d = 2
        for i in range(2, int((cif / 2) + 1)):
            if cif % i == 0:
                d += 1
    print(d)

def gipo():
    a = int(input("Введите число A: "))
    b = int(input("Введите число B: "))
    c = math.sqrt(a * a + b * b)
    print(f"Гипотенуза этих чисел равна: {c}")

def find_square_root():
    num = float(input("Введите число: "))
    if num < 0:
        print("Невозможно вычислить квадратный корень из отрицательного числа")
    else:
        result = math.sqrt(num)
        print("Квадратный корень числа", num, "равен", result)

def factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def gcd_lcm():
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    print(f"Наибольший общий делитель (НОД) чисел {num1} и {num2} равен: {gcd(num1, num2)}")
    print(f"Наименьшее общее кратное (НОК) чисел {num1} и {num2} равно: {lcm(num1, num2)}")

while True:
    print("""
    ██░░██░░░░░░█░░░████████░░░██░░░██░░░░░░████
    █░██░█░░░░░█░█░░░░░██░░░░░░██░░░██░░░░░██████
    █░░░░█░░░░█████░░░░██░░░░░░███████░░░░░██░░░░
    █░░░░█░░░██░░░██░░░██░░░░░░██░░░██░░░░░░████░
    █░░░░█░░░██░░░██░░░██░░░░░░██░░░██░░░░░░░░░██
    █████████████████████████████████████████████
    """)

    print("-----[MATH]-----")
    print("[1] Переводчик систем счисления")
    print("[2] Возведение любого числа в степень")
    print("[3] Модуль числа")
    print("[4] Пифагоровы тройки")
    print("[5] Количество делителей")
    print("[6] Гипотенуза")
    print("[7] Корень числа")
    print("[8] Факториал")
    print("[9] Калькулятор")
    print("[10] НОК и НОД")
    func = int(input("Выберите нужную функцию: "))

    if func == 1:
        sistsch()
    elif func == 2:
        stepeni()
    elif func == 3:
        modul()
    elif func == 4:
        pif3()
    elif func == 5:
        delit()
    elif func == 6:
        gipo()
    elif func == 7:
        find_square_root()
    elif func == 8:
        num = int(input("Введите число факториал которого нужно посчитать: "))
        print(f"Факториал {num} равен {factorial(num)}")
    elif func == 9:
        calculator()
    elif func == 10:
        gcd_lcm()
    
    repeat = input("Хотите выполнить еще одну операцию? (да/нет): ")
    if repeat.lower() != 'да':
        break
