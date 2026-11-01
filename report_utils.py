import math
def create_report(expenses, month):
    total = 0

    print("\n----- MONTHLY EXPENSE REPORT -----")

    for expense in expenses:
        if expense["date"][0:7] == month:
            print("Reference ID:", expense["id"])
            print("Date:", expense["date"])
            print("Description:", expense["description"])
            print("Category:", expense["category"])
            print("Amount:", round(expense["amount"], 2))

            print("----------------------------")

            total = total + expense["amount"]

    print("Total spending:", round(total, 2))
    print("Report month:", month)