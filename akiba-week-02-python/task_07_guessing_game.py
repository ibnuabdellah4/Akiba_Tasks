secret_num = 33

attempts = 0
guess = int(input(f"Guess the secret number between 1 and 100 ({5 - attempts} attempts left): "))

while guess != secret_num:
    attempts += 1
    if guess < secret_num:
        print("Guess higher.")
    else:
        print("Guess lower.")
    
    guess = int(input(f"Guess the secret number between 1 and 100 ({5 - attempts} attempts left): "))

    if attempts >= 4:
        print("Sorry, you've reached the maximum number of attempts. The secret number was 33.")
        break
print(f"Congratulations! You guessed the secret number in {attempts} attempts.")
