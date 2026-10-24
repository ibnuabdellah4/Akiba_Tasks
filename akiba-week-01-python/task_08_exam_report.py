student_name = input("Enter student name: ")
python_score = float(input("Enter Python score: "))
english_score = float(input("Enter English score: "))
math_score = float(input("Enter Math score: "))
avg = (python_score + english_score + math_score) / 3
result = f'''
======================
    STUDENT RESULT
======================
Name: {student_name}
Python: {python_score}
English: {english_score}
Math: {math_score}
----------------------
Average: {avg}
======================
'''
print(result)
