import json
from datetime import datetime

DATA_FILE = "operations.json"

def load_operations():
    """Загружает операции из файла."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_operations(operations):
    """Сохраняет операции в файл."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(operations, f, ensure_ascii=False, indent=2)

def add_operation(operations):
    """Добавляет новую операцию (доход или расход)."""
    print("\n--- Добавление операции ---")
    op_type = input("Тип (доход/расход): ").strip().lower()
    if op_type not in ["доход", "расход"]:
        print("Ошибка: тип должен быть 'доход' или 'расход'.")
        return

    try:
        amount = float(input("Сумма: "))
    except ValueError:
        print("Ошибка: сумма должна быть числом.")
        return

    category = input("Категория: ").strip()
    date_input = input("Дата (ГГГГ-ММ-ДД) или Enter для сегодня: ").strip()
    
    if not date_input:
        date = datetime.now().strftime("%Y-%m-%d")
    else:
        date = date_input

    operations.append({
        "type": op_type, 
        "amount": amount,
        "category": category, 
        "date": date
    })
    save_operations(operations)
    print("Операция успешно добавлена!")

def show_operations(operations):
    """Выводит список всех операций."""
    print("\n--- Список операций ---")
    if not operations:
        print("Операций пока нет.")
        return
    
    for i, op in enumerate(operations, 1):
        print(f"{i}. {op['date']} | {op['type'].capitalize()} | {op['amount']} руб. | {op['category']}")

def show_balance(operations):
    """Считает и выводит текущий баланс."""
    print("\n--- Текущий баланс ---")
    income = sum(op["amount"] for op in operations if op["type"] == "доход")
    expense = sum(op["amount"] for op in operations if op["type"] == "расход")
    
    print(f"Общий доход: {income} руб.")
    print(f"Общий расход: {expense} руб.")
    print(f"Текущий баланс: {income - expense} руб.")


def main():
    """Главная функция запуска приложения."""
    operations = load_operations()
    
    while True:
        print("\n=== Калькулятор личных финансов ===")
        print("1. Добавить операцию")
        print("2. Показать все операции")
        print("3. Показать баланс")
        print("0. Выход")
        
        choice = input("Выберите пункт меню: ").strip()
        
        if choice == "1":
            add_operation(operations)
        elif choice == "2":
            show_operations(operations)
        elif choice == "3":
            show_balance(operations)
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
