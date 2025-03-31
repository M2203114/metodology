import random


def generate_progression():
    """Generates a geometric progression."""
    length = random.randint(5, 10)
    start = random.randint(1, 5)
    ratio = random.randint(2, 5)

    progression = []
    current = start
    for _ in range(length):
        progression.append(current)
        current *= ratio

    return progression


def format_question(progression, hidden_index):
    """Format the progression with hidden number."""
    return ['..' if i == hidden_index else str(num) 
            for i, num in enumerate(progression)]


def check_answer(user_answer, correct_answer, name):
    """Check if the user's answer is correct."""
    if user_answer == correct_answer:
        print("Correct!\n")
        return True
    print(f"'{user_answer}' is wrong answer ;(. "
          f"Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {name}!")
    return False


def play_round(name):
    """Play a single round of the game."""
    progression = generate_progression()
    hidden_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[hidden_index]
    
    question = format_question(progression, hidden_index)
    print(f"Question: {' '.join(question)}")
    user_answer = int(input("Your answer: "))
    return check_answer(user_answer, correct_answer, name)


def play_game():
    """Plays the Brain Games progression game."""
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?\n")

    correct_answers = 0
    total_questions = 3

    for _ in range(total_questions):
        if not play_round(name):
            return
        correct_answers += 1

    print(f"Congratulations, {name}!")


play_game()
