word = input("Enter a word: ")
word_format = word.lower()

if word_format == word_format[::-1]:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")