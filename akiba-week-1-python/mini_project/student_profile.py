full_name = input("Enter student's full name: ")
age = int(input("Enter student's age: "))
id = input("Enter student's ID: ")
city = input("Enter student's city: ")
university = input("Enter student's university: ")
department = input("Enter student's department: ")
email = input("Enter student's email: ")
phone = int(input("Enter student's phone: "))
fav_prog_lang = input("Enter student's favorite programming language: ")
prog_goal = input("Enter student's programming goal: ")

student_profile = f'''
=============================
    AKIBA STUDENT PROFILE
=============================

Name: {full_name}
Age: {age}
Student ID: {id}
City: {city}
University: {university}
Department: {department}
Email: {email}
Phone: {phone}
Favorite Programming Language: {fav_prog_lang}

Programming Goal:
{prog_goal}

=============================
'''
print(student_profile)
