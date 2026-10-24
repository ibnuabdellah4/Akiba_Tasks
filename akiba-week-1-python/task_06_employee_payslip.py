employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
transport_allowance = float(input("Enter transport allowance: "))
food_allowance = float(input("Enter food allowance: "))
gross_salary = basic_salary + transport_allowance + food_allowance
payslip = f'''
===============================
    EMPLOYEE PAYSLIP
===============================
Employee Name: {employee_name}
Basic Salary: {basic_salary}
Transport Allowance: {transport_allowance}
Food Allowance: {food_allowance}
-------------------------------
Gross Salary: {gross_salary}
===============================
'''
print(payslip)
