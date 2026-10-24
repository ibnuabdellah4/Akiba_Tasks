numbers = []

even_count = 0
odd_count = 0
print("Please enter 10 numbers:")
for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    numbers.append(num)

largest = max(numbers)
smallest = min(numbers)
total_sum = sum(numbers)
average = total_sum / len(numbers)

print(f"""Numbers entered: {numbers}
1. Largest number: {largest}
2. Smallest number: {smallest}
3. Total sum: {total_sum}
4. Average: {average}
5. Even numbers count: {even_count}
6. Odd numbers count: {odd_count}""")