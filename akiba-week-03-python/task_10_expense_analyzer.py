def add_expense(expenses):
    description = input("Enter expense description: ").strip()
    category = input("Enter category (e.g., Food, Transport, Bills): ").strip()
    amount = float(input("Enter amount: ").strip())
    
    if amount <= 0:
        print("Amount must be greater than zero.\n")
        return

    expenses.append({"description": description, "category": category, "amount": amount})
    print("Expense added successfully!\n")

def calculate_total_expenses(expenses):
    total = 0
    for exp in expenses:
        total += exp["amount"]
    return total

def calculate_spending_by_category(expenses):
    category_spending = {}
    for exp in expenses:
        cat = exp["category"]
        category_spending[cat] = category_spending.get(cat, 0) + exp["amount"]
    return category_spending

def find_largest_expense(expenses):
    if not expenses:
        return None
    largest = expenses[0]
    for exp in expenses:
        if exp["amount"] > largest["amount"]:
            largest = exp
    return largest

def identify_expenses_above_threshold(expenses, threshold):
    return [exp for exp in expenses if exp["amount"] > threshold]

def generate_spending_report(expenses):
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    total = calculate_total_expenses(expenses)
    print(f"\n===== SPENDING REPORT =====")
    print(f"Total Expenses: {total} Birr\n")

    print("Spending by Category:")
    cat_spending = calculate_spending_by_category(expenses)
    for cat, amount in cat_spending.items():
        percentage = (amount / total) * 100 if total > 0 else 0
        print(f"  - {cat}: {amount} Birr ({percentage:.2f}%)")

    largest = find_largest_expense(expenses)
    if largest:
        print(f"\nLargest Expense: {largest['description']} ({largest['amount']} Birr in [{largest['category']}])")

    if cat_spending:
        highest_cat = max(cat_spending, key=cat_spending.get)
        print(f"Highest Spending Category: {highest_cat} ({cat_spending[highest_cat]} Birr)")

    threshold = float(input("\nEnter a threshold amount to view expenses above it: "))
    above_threshold = identify_expenses_above_threshold(expenses, threshold)
    print(f"Expenses above {threshold} Birr:")
    if above_threshold:
        for exp in above_threshold:
            print(f"  - {exp['description']} ({exp['category']}): {exp['amount']} Birr")
    else:
        print("  None found.")
        print("===========================")

expenses = [
    {"description": "Lunch", "category": "Food", "amount": 180},
    {"description": "Taxi", "category": "Transport", "amount": 120},
    {"description": "Groceries", "category": "Food", "amount": 450},
    {"description": "Internet", "category": "Bills", "amount": 300}
]

while True:
    print("===== EXPENSE ANALYZER =====")
    print("1. Add Expense")
    print("2. Generate Spending Report")
    print("3. Exit")
    choice = input("Choose an option (1-3): ").strip()

    if choice == "1":
        add_expense(expenses)
    elif choice == "2":
        generate_spending_report(expenses)
    elif choice == "3":
        print("Exiting Expense Analyzer. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.\n")