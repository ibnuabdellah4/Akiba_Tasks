balance = 1000
pin = 1234
attempt = 0

user_pin = int(input("Enter your PIN: "))
attempt += 1
if user_pin == 1234:
    print("Access granted.")
    choice = int(input("""
    == AKIBA BANK ====
    1. Check Balance
    2. Deposit Money
    3. Withdraw Money
    4. Exit

    Choice:"""))


    if choice == 1:
        print(f'Your current balance is {balance}birr')
    elif choice == 2:
        deposit = float(input("Enter the amount of money that you want to deposit: "))
        if deposit > 0:
            balance += deposit
            print(f'You have deposited {deposit}birr. Your current balance is {balance}birr')
        else:
            print('Invalid Deposit Amount. Please try again')
    elif choice == 3:
        withdraw = float(input("Enter the amount of money that you want to withdraw: "))
        if 0 < withdraw <= balance:
            balance -= withdraw
            print(f'You have withdrawn {withdraw}birr. Your current balance is {balance}birr')
        else:
            print('Invalid Withdrawal Amount or Insufficient Funds. Please try again')
    elif choice == 4:
        print('Thank you for using Akiba Bank! \n Goodbye!')
    else:
        print('Invalid Choice. Please try again')
else:
    while attempt < 3:
        attempt += 1
        print("Invalid PIN. Please try again. Attempts left:", 3 - attempt)
        if attempt == 3:
            print("Access denied. Please contact the bank.")
            break
