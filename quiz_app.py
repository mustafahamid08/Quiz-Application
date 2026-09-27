questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language is mainly used for web page structure?",
        "options": ["Python", "HTML", "SQL", "C++"],
        "answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Personal Unit",
            "Central Program Utility",
            "Computer Processing User"
        ],
        "answer": "A"
    },
    {
        "question": "Which data type stores True or False in Python?",
        "options": ["String", "Integer", "Boolean", "Float"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "define", "def", "fun"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": "B"
    },
    {
        "question": "Which of these is a Python data structure?",
        "options": ["List", "Browser", "Compiler", "Monitor"],
        "answer": "A"
    },
    {
        "question": "What is the extension of a Python file?",
        "options": [".html", ".java", ".py", ".cpp"],
        "answer": "C"
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": ["input()", "display()", "show()", "print()"],
        "answer": "D"
    },
    {
        "question": "Which loop is commonly used to iterate over a sequence in Python?",
        "options": ["for", "repeat", "loop", "iterate"],
        "answer": "A"
    }
]


def run_quiz():
    score = 0

    print("\n================================")
    print("        QUIZ APPLICATION")
    print("================================\n")

    for number, question in enumerate(questions, start=1):

        print(f"Question {number}: {question['question']}\n")

        for index, option in enumerate(question["options"]):
            print(f"{chr(65 + index)}. {option}")

        while True:
            answer = input("\nEnter your answer (A/B/C/D): ").strip().upper()

            if answer in ["A", "B", "C", "D"]:
                break

            print("Invalid input! Please enter A, B, C, or D.")

        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct answer is {question['answer']}.\n")

    total = len(questions)
    percentage = (score / total) * 100

    print("================================")
    print("        QUIZ COMPLETED")
    print("================================")
    print(f"Your Score: {score}/{total}")
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 80:
        print("Excellent Performance!")
    elif percentage >= 60:
        print("Good Performance!")
    elif percentage >= 40:
        print("Keep Practicing!")
    else:
        print("Keep Learning and Try Again!")

    print("================================")


while True:
    run_quiz()

    choice = input("\nDo you want to play again? (y/n): ").strip().lower()

    if choice != "y":
        print("\nThank You For Playing!")
        break