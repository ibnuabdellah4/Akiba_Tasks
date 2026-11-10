def display_question(q_data):
    print(q_data["question"])
    for opt in q_data["options"]:
        print(opt)

def validate_answer():
    ans = input("Enter your answer (A, B, C, D): ").strip().upper()
    while ans not in ["A", "B", "C", "D"]:
        print("Invalid option. Please choose A, B, C, or D.")
        ans = input("Enter your answer (A, B, C, D): ").strip().upper()
    return ans

def check_answer(user_ans, correct_ans):
    return user_ans == correct_ans

def run_quiz():
    questions = [
        {
            "question": "1. What is the file extension for Python files?",
            "options": ["A) .pt", "B) .py", "C) .python", "D) .pi"],
            "answer": "B"
        },
        {
            "question": "2. Which keyword is used to define a function in Python?",
            "options": ["A) func", "B) define", "C) def", "D) function"],
            "answer": "C"
        },
        {
            "question": "3. Which of these is a mutable data type in Python?",
            "options": ["A) Tuple", "B) String", "C) List", "D) Integer"],
            "answer": "C"
        },
        {
            "question": "4. How do you write a single-line comment in Python?",
            "options": ["A) //", "B) /*", "C) #", "D) <!--"],
            "answer": "C"
        },
        {
            "question": "5. Which built-in function gives the length of a list?",
            "options": ["A) length()", "B) size()", "C) count()", "D) len()"],
            "answer": "D"
        }
    ]
    
    score = 0
    incorrect = 0
    
    for q in questions:
        display_question(q)
        user_ans = validate_answer()
        if check_answer(user_ans, q["answer"]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")
            incorrect += 1
            
    total_questions = len(questions)
    percentage = (score / total_questions) * 100
    
    print(f"""
    === QUIZ RESULTS ===)
    Correct answers: {score}
    Incorrect answers: {incorrect}
    Final Score: {percentage}%
    """)
    
    # Challenge: Result Category
    if percentage >= 90:
        category = "Outstanding"
    elif percentage >= 75:
        category = "Good"
    elif percentage >= 50:
        category = "Pass"
    else:
        category = "Needs Improvement"
        
    print(f"Result Category: {category}")

while True:
        run_quiz()
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break