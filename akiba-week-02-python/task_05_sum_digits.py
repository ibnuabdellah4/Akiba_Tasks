num = input("Enter a number: ")
sum = 0
for digit in num:
    sum += int(digit)
print(f"The sum of the digits in {num} is {sum}")