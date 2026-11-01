import datetime as dt
import random
import expense_utils as eu
import report_utils
from tabulate import tabulate

expenses = []

print("Personal Expense Tracker")

while True:
    description = input("Enter description:")
    category = input("Enter category:")
    amount = float(input("Enter amount:"))

    if eu.validate_amount(amount) == False:
        print("Amount must be positive")
        continue

    date = input("Enter date (YYYY-MM-DD, blank for today):")

    if date == "":
        date = dt.date.today().strftime("%Y-%m-%d")

    reference_id = "EXP-" + str(random.randint(100000, 999999))

    expense = {
        "id": reference_id,
        "date": date,
        "description": description,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    print("Reference ID:", reference_id)

    choice = input("Add another expense? (yes/no):")

    if choice == "no":
        break

print("\nAll Expenses")

table = []

for expense in expenses:
    row = [
        expense["id"],
        expense["date"],
        expense["description"],
        expense["category"],
        expense["amount"]
    ]

    table.append(row)

print(tabulate(
    table,
    headers=["ID", "Date", "Description", "Category", "Amount"],
    tablefmt="grid"
))

total = eu.calculate_total(expenses)

print("\nTotal spending:", round(total, 2))

categories = eu.category_total(expenses)

print("\nCategory-wise Expenses")

for category in categories:
    print(category, ":", round(categories[category], 2))

current_month = dt.date.today().strftime("%Y-%m")

report_utils.create_report(expenses, current_month)