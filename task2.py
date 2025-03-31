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


def play_game():
    """Plays the Brain Games progression game."""
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?\n")

    correct_answers = 0
    total_questions = 3

    for _ in range(total_questions):
        progression = generate_progression()
        hidden_index = random.randint(0, len(progression) - 1)
        correct_answer = progression[hidden_index]

        # Create question string with hidden number
        question = []
        for i, num in enumerate(progression):
            if i == hidden_index:
                question.append('..')
            else:
                question.append(str(num))

        print(f"Question: {' '.join(question)}")
        user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print("Correct!\n")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    if correct_answers == total_questions:
        print(f"Congratulations, {name}!")


play_game()
