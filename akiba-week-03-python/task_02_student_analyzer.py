def validate_score(score):
    if score < 0 or score > 100:
        return "Error: Score must be between 0 and 100."
    return True

def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def calculate_average(students):
    total = 0
    for s in students:
        total += s["score"]
    return total / len(students)

def find_highest_lowest(students):
    highest = students[0]
    lowest = students[0]
    for s in students[1:]:
        if s["score"] > highest["score"]:
            highest = s
        if s["score"] < lowest["score"]:
            lowest = s
    return highest, lowest

def count_pass_fail(students):
    passed = 0
    failed = 0
    for s in students:
        if s["score"] >= 50:
            passed += 1
        else:
            failed += 1
    return passed, failed

def generate_report(students):
    avg = calculate_average(students)
    highest, lowest = find_highest_lowest(students)
    passed, failed = count_pass_fail(students)
    
    above_avg = []
    for s in students:
        if s["score"] > avg:
            above_avg.append(s)
            
    return {
        "average": avg,
        "highest": highest,
        "lowest": lowest,
        "passed": passed,
        "failed": failed,
        "above_average": above_avg
    }

students = [
    {"name": "Sara", "score": 85},
    {"name": "Ahmed", "score": 42},
    {"name": "Musa", "score": 93},
    {"name": "Hana", "score": 67}
]

print(generate_report(students))