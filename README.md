# File: README.md

# Personal Expenses Tracker
A local comman-line program that tracks daily expenses. 
It loads an interactive terminal where you key in:
 1 - to add expenses,
  2 - to getr list of expenses,
   3 - to load the summary and lastly
    4 - to close the interactive terminal. 

## What It Does

- Prints a menu in the terminal 
- Reads what  you type
- Accepts data input for expense
- On command, it prints the summary of expenses
- Exports saved report as JSON

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```python
def list_expenses():
    expenses = load_expenses()

 print(f"{'#':<4} {'amount':>8}  {'category':<13} {'note':<13} {'date':>16}")
    print("-" * 60)

for i, item in enumerate(expenses, start=1):
        print(f"{i:<4} {item['amount']:>8.2f}  {item['category']:<13} {item['note']:<13} {item.get('spent_on', item.get('date', '-')):>16}")
```

## Sample Output

```
#      amount  category      note                      date
------------------------------------------------------------

4      300.00  food          lunch               2026-09-30
5      500.00  gift          school book         2026-09-30
```

## Stack

Python

Built-in Modules: `json`, `pathlib`, `datetime`