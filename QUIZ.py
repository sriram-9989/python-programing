import random

# Quiz questions with format (question, answer)
quiz_questions = [
    ("What is the capital of France?", "Paris"),
    ("Who wrote 'Romeo and Juliet'?", "William Shakespeare"),
    ("What is the chemical symbol for water?", "H2O"),
    ("How many continents are there?", "7"),
    ("What is the largest mammal?", "Blue whale")
]

def display_intro():
    print("Welcome to the Quiz Game!")
    print("You will be asked multiple-choice and fill-in-the-blank questions.")
    print("Let's begin!\n")

def ask_question(question, correct_answer):
    user_answer = input(question + " ").strip().lower()
    if user_answer == correct_answer.lower():
        print("Correct!")
        return True
    else:
        print("Incorrect. The correct answer is:", correct_answer)
        return False

def play_quiz():
    score = 0
    random.shuffle(quiz_questions)
    for question, answer in quiz_questions:
        if ask_question(question, answer):
            score += 1
    print("\nQuiz completed!")
    print("Your final score is:", score, "out of", len(quiz_questions))
    print("Thank you for playing!")

def main():
    display_intro()
    play_quiz()
    while input("Do you want to play again? (yes/no): ").lower() == "yes":
        play_quiz()

if __name__ == "__main__":
    main()
