# Expense Tracker
from datetime import date, datetime, datetime
import json
from pathlib import Path

DATA_FILE = Path("expenses.json")


def load_expenses():
    if not DATA_FILE.exists():
        return []
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def save_expenses(expenses):
    DATA_FILE.write_text(json.dumps(expenses, indent=2), encoding="utf-8")


def add_expense():
    amount_text = input("Amount: ").strip()
    try:
        amount = float(amount_text)
    except ValueError:
        print("Please type a number, for example 12.50")
        return

    category = input("Category (food, transport, ...): ").strip()
    if not category:
        print("Category cannot be empty.")
        return

    note = input("Note (optional): ").strip()
    date_text = input("Date (YYYY-MM-DD, optional): ").strip()
    
    if date_text == "":
            spent_on = date.today().isoformat()
    else:
            try:
                spent_on = datetime.strptime(date_text, "%Y-%m-%d").date().isoformat()
            except ValueError:
                print("Please use YYYY-MM-DD, for example 2026-09-30")
                return

    expenses = load_expenses()
    expenses.append({"amount": amount, "category": category.lower(), "note": note, "date": spent_on})
    save_expenses(expenses)
    print("Saved.")


def list_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses yet.")
        return

    print()
    print(f"{'#':<4} {'amount':>8}  {'category':<13} {'note':<13} {'date':>16}")
    print("-" * 60)
    total = 0
    for i, item in enumerate(expenses, start=1):
        print(f"{i:<4} {item['amount']:>8.2f}  {item['category']:<13} {item['note']:<13} {item.get('spent_on', item.get('date', '-')):>16}")
        total += item["amount"]
    print("-" * 60)
    print(f"Total: {total:.2f}")


def show_summary():
    expenses = load_expenses()
    if not expenses:
        print("No expenses yet.")
        return

    totals = {}
    for item in expenses:
        category = item["category"]
        totals[category] = totals.get(category, 0) + item["amount"]

    print()
    print(f"{'category':<16} {'total':>8}")
    print("-" * 28)
    for category, total in totals.items():
        print(f"{category:<16} {total:>8.2f}")


def show_menu():
    print()
    print("1. Add expense")
    print("2. List expenses")
    print("3. Summary")
    print("4. Quit")


def main():
    print("Expense Tracker")
    while True:
        show_menu()
        choice = input("Choose 1-4: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            list_expenses()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            print("Bye.")
            break
        else:
            print("Type 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
