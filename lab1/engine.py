import prompt

ROUNDS_COUNT = 3

def run_game(game_rules, generate_question_and_answer):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game_rules)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = generate_question_and_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer != str(correct_answer):
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")