correct_pin = "1234"
max_attempts = 3
attempts = 0
while attempts != max_attempts:
    pin = input(f"Enter your PIN ({max_attempts - attempts} attempts left): ")
    if pin == correct_pin:
        print("PIN is correct.")
        break
    else:
        print("Incorrect PIN.")
        attempts += 1
else:
    print("Too many incorrect attempts.")