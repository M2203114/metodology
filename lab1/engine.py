from typing import Callable, Tuple


def run_game(
    game_description: str, generate_round: Callable[[], Tuple[str, str]]
) -> None:
    """Run the main game engine."""
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(game_description)

    for _ in range(3):
        question, correct_answer = generate_round()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer != correct_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
