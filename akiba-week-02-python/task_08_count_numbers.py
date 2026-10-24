num = int(input("Enter a number: "))
if num > 0:
    even_count = 0
    odd_count = 0
    total_sum = 0
    for i in range(1, num + 1):
        total_sum += i
        if i % 2 == 0:
            status = "even"
            even_count += 1
        else:
            status = "odd" 
            odd_count += 1
        print(f"{i}({status})")
    msg = f'''
    Total even numbers: {even_count}
    Total odd numbers: {odd_count}
    Total sum: {total_sum}'''
    
    print(msg)
else:
    print("The number is not positive and/or greater than 1.")