def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    return total


def category_total(expenses):
    categories = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] = categories[category] + amount
        else:
            categories[category] = amount
            return categories


def validate_amount(amount):
    if amount > 0:
        return True
    else:
        return False