#Автор: Терещук Д.В., Группа ПРЗ-23, 15.11.2026
def main():
    print("Калькулятор")

    try:
        first_number = float(input("Введите первое число: "))
        second_number = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: необходимо вводить числа, а не буквы.")
        print("Дробные числа вводите через точку, например: 2.5")
        return

    operation = input("Введите операцию (+, -, *, /, **): ").strip()

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            print("Ошибка: делить на ноль нельзя.")
            return
        result = first_number / second_number
    elif operation == "**":
        try:
            result = first_number ** second_number
        except ZeroDivisionError:
            print("Ошибка: ноль нельзя возводить в отрицательную степень.")
            return
        except OverflowError:
            print("Ошибка: результат возведения в степень слишком большой.")
            return
    else:
        print("Ошибка: неизвестная операция. Используйте +, -, *, / или **.")
        return

    print(f"Результат: {result}")

if __name__ == "__main__":
    main()
