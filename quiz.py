print("===== QUIZ GAME =====")

score = 0

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Hyderabad"],
        "answer": "b"
    },
    {
        "question": "Which language are we learning?",
        "options": ["A. Java", "B. C++", "C. Python", "D. HTML"],
        "answer": "c"
    },
    {
        "question": "What is 10 + 5?",
        "options": ["A. 15", "B. 20", "C. 10", "D. 25"],
        "answer": "a"
    },
    {
        "question": "Which one is a Python data type?",
        "options": ["A. Integer", "B. Browser", "C. Keyboard", "D. Monitor"],
        "answer": "a"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. /* */", "D. --"],
        "answer": "b"    }
]


def run_quiz():
    global score

    for number, quiz in enumerate(questions, start=1):
        print(f"\n{number}. {quiz['question']}")

        for option in quiz["options"]:
            print(option)

        answer = input("Enter your answer: ").lower()

        if answer == quiz["answer"]:
            print("Correct! 🎉")
            score += 1
        else:
            print("Wrong!")


def show_result():
    total = len(questions)
    percentage = (score / total) * 100

    print("\n===== QUIZ FINISHED =====")
    print("Your score:", score, "/", total)
    print("Percentage:", percentage, "%")

    if percentage == 100:
        print("Excellent! 🏆")
    elif percentage >= 60:
        print("Good job! 👍")
    elif percentage >= 40:
        print("Keep practicing! 💪")
    else:
        print("You need more practice. 📚")


while True:
    score = 0

    run_quiz()
    show_result()

    play_again = input(
        "\nDo you want to play again? (yes/no): "
    ).lower()

    if play_again != "yes":
        print("Thanks for playing! 👋")
        break