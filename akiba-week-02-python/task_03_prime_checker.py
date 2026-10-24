num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is not Prime")
elif num == 2:
    print(f"{num} is Prime")
else:
    is_prime = True
    # We only check for factors up to the square root of the number but not including 1 and the number itself.
    limit = int(num**0.5)
    for i in range(2, limit + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is Prime")
    else:
        print(f"{num} is not Prime")
