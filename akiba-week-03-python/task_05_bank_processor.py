balance = 1000
history = []
daily_withdrawn = 0
daily_limit = 2000

def deposit(amount):
    global balance
    if amount <= 0:
        print("Invalid amount! Cannot deposit zero or negative numbers.")
    else:
        balance = balance + amount
        # record transaction
        record = {"type": "deposit", "amount": amount, "balance_after": balance}
        history.append(record)
        print("Deposited:", amount)

def withdraw(amount):
    global balance, daily_withdrawn
    if amount <= 0:
        print("Invalid amount!")
    elif amount > balance:
        print("You don't have enough money in your account!")
    elif daily_withdrawn + amount > daily_limit:
        print("Withdrawal failed! Daily limit reached.")
    else:
        balance = balance - amount
        daily_withdrawn = daily_withdrawn + amount
        record = {"type": "withdrawal", "amount": amount, "balance_after": balance}
        history.append(record)
        print("Withdrew:", amount)

def check_balance():
    print("Current balance is:", balance)

def generate_summary():
    print("\n--- Summary ---")
    print("Final Balance:", balance)
    
    total_dep = 0
    total_wit = 0
    for t in history:
        if t["type"] == "deposit":
            total_dep = total_dep + t["amount"]
        else:
            total_wit = total_wit + t["amount"]
            
    print("Total Deposited:", total_dep)
    print("Total Withdrawn:", total_wit)
    
    print("\nHistory:")
    for t in history:
        print(t)

deposit(500)
withdraw(200)
check_balance()
generate_summary()