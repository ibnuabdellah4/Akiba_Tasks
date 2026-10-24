name = input("Enter your name: ")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
report = f'''
==================
   BMI REPORT
==================
Name: {name}
Weight: {weight} kg
Height: {height} m
BMI: {bmi:.2f}
'''
print(report)
