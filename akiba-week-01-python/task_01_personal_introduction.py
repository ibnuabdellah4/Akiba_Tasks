name = input("What is your name?: ")
age = input("How old are you?: ")
city = input("What city do you live in?: ")
university = input("What university do you go to?: ")
department = input("Which department do you study?: ")
fav_prog_lang = input("What is your favorite programming language?: ")
prog_goal = input("What is your programming goal?: ")

student_intro = f'''
====================
STUDENT INTRODUCTION
====================
My name is {name}.
I am {age} years old.
I live in {city}.
I study {department} at {university}.
My favorite programming language is {fav_prog_lang}.
My programming goal:
{prog_goal}.
===================
'''
print(student_intro)
