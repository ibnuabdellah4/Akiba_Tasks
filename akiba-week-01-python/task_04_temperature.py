print('''
Choose the conversion that you want:
    1. Celsius to Fahrenheit
    2. Fahrenheit to Celsius
    ''')
choice = int(input("Enter your choice: "))

if choice == 1:
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C in fahrenheit is {fahrenheit}°F")
elif choice == 2:
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F in celsius is {celsius}°C")
else:
    print("Invalid choice. We only accept 1 or 2.")
