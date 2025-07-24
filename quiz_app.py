import json


def load_questions(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: questions.json not found!")
        return []


def run_quiz(questions):
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q['options']:
            print(option)
        
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        
        if answer == q['answer'].upper():
            print(" Correct!")
            score += 1
        else:
            print(f" Wrong! Correct answer was: {q['answer']}")

    print(f"\n Quiz complete! You scored {score}/{len(questions)}.")


def main():
    questions = load_questions("questions.json")
    if questions:
        print(" Welcome to the Quiz App!")
        run_quiz(questions)

if __name__ == "__main__":
    main()
