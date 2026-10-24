def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def sum_of_digits(num):
    total = 0
    for digit in str(num):
        total += int(digit)
    return total

def reverse_number(num):
    reversed = int(str(num)[::-1])
    return reversed

def analyze_number(num):
    analysis = {
        "is_prime": is_prime(num),
        "divisors": get_divisors(num),
        "sum_of_digits": sum_of_digits(num),
        "reversed_number": reverse_number(num)
    }
    return analysis

num = int(input("Enter a number: "))
if num > 0:
    result = analyze_number(num)
    print(f"""
    === Analysis of {num} ===

    Is Prime: {result['is_prime']}
    Divisors: {result['divisors']}
    Sum of Digits: {result['sum_of_digits']}
    Reversed Number: {result['reversed_number']}""")
else:
    print("Error: Please enter a positive integer.")