"""
Главный модуль приложения Калькулятор.
Отвечает за взаимодействие с пользователем.
"""
import calc_logic  # Импортируем наш новый модуль

def get_number(prompt: str) -> float:
    """Запрашивает у пользователя число с обработкой ошибок."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число!")

def main():
    print("=== Модульный Калькулятор v2.0 ===")

    operation = input(
        "Выберите операцию (+, -, *, /, sqrt): "
    ).strip().lower()

    if operation not in ("+", "-", "*", "/", "sqrt"):
        print("Неизвестная операция!")
        return

    try:
        if operation == "sqrt":
            num = get_number("Введите число для извлечения корня: ")
            result = calc_logic.square_root(num)
        else:
            num1 = get_number("Введите первое число: ")
            num2 = get_number("Введите второе число: ")

            if operation == "+":
                result = calc_logic.add(num1, num2)
            elif operation == "-":
                result = calc_logic.subtract(num1, num2)
            elif operation == "*":
                result = calc_logic.multiply(num1, num2)
            elif operation == "/":
                result = calc_logic.divide(num1, num2)

        print(f"Результат: {result}")

    except (ValueError, ZeroDivisionError) as error:
        print(f"Ошибка вычисления: {error}")

if __name__ == "__main__":
    main()
