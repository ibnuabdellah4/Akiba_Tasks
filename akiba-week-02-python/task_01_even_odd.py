num = int(input('Enter a number: '))
remainder = num%2
if num == 0:
    print('0 is an even number')
else:
    if remainder == 0 and num > 0:
        print(f'{num} is a positive even number')
    elif remainder != 0 and num > 0:
        print(f'{num} is a positive odd number')
    elif remainder == 0 and num < 0:
        print(f'{num} is a negative even number')
    elif remainder != 0 and num < 0:
        print(f'{num} is a negative odd number')
    else:
        print('Invalid Input')