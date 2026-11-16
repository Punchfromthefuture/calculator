"""
Главный модуль приложения Калькулятор.
Отвечает за взаимодействие с пользователем.
"""
import calc_logic  # Импортируем наш новый модуль
import db_manager

def get_number(prompt: str) -> float:
    """Запрашивает у пользователя число с обработкой ошибок."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число!")

def main():
    print("=== Модульный Калькулятор v3.0 (с историей) ===")

    db_manager.init_db()

    while True:
        print("\n--- Меню ---")
        print("1. Выполнить вычисление")
        print("2. Показать историю (последние 10)")
        print("3. Очистить историю")
        print("4. Показать статистику")
        print("5. Найти записи в истории")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == '0':
            print("До свидания!")
            break
        elif choice == '1':
            perform_calculation()
        elif choice == '2':
            show_history()
        elif choice == '3':
            db_manager.clear_history()
            print("История очищена.")
        elif choice == '4':
            show_statistics()
        elif choice == '5':
            find_history()
        else:
            print("Неверный выбор. Попробуйте снова.")

def perform_calculation():
    """Выполняет вычисление и сохраняет результат в БД."""
    num1 = get_number("Введите первое число: ")
    num2 = get_number("Введите второе число: ")
    operation = input("Выберите операцию (+, -, *, /): ")

    try:
        if operation == '+':
            result = calc_logic.add(num1, num2)
        elif operation == '-':
            result = calc_logic.subtract(num1, num2)
        elif operation == '*':
            result = calc_logic.multiply(num1, num2)
        elif operation == '/':
            result = calc_logic.divide(num1, num2)
        else:
            print("Неизвестная операция!")
            return

        expression = f"{num1} {operation} {num2}"
        db_manager.save_record(expression, result)
        print(f"Результат: {result}")

    except (ValueError, ZeroDivisionError) as error:
        print(f"Ошибка вычисления: {error}")

def show_history():
    """Показывает последние 10 записей из истории."""
    history = db_manager.get_history(10)

    if not history:
        print("История пуста.")
        return

    print("\n--- История вычислений ---")
    for record in history:
        print(f"  [{record[3]}] {record[1]} = {record[2]}")

def show_statistics():
    """Выводит статистику вычислений или сообщение о пустой истории."""
    statistics = db_manager.get_statistics()

    if statistics["count"] == 0:
        print("История пуста. Статистика пока недоступна.")
        return

    print("\n--- Статистика вычислений ---")
    print(f"Всего вычислений: {statistics['count']}")
    print(f"Средний результат: {statistics['average']}")
    print(f"Максимальный результат: {statistics['maximum']}")
    print(f"Минимальный результат: {statistics['minimum']}")

def find_history():
    """Запрашивает текст поиска и выводит найденные записи истории."""
    keyword = input("Введите фрагмент выражения для поиска: ").strip()

    if not keyword:
        print("Ошибка: поисковый запрос не должен быть пустым.")
        return

    records = db_manager.search_history(keyword)

    if not records:
        print("Записи не найдены.")
        return

    print(f"\n--- Найдено записей: {len(records)} ---")
    for record in records:
        print(f"  [{record[3]}] {record[1]} = {record[2]}")

if __name__ == "__main__":
    main()
