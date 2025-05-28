import random

from games.engine import run_game


def generate_round():
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    progression = [str(start * step ** i) for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    answer = progression[hidden_index]
    progression[hidden_index] = ".."
    question = " ".join(progression)
    return question, answer

def main():
    rules = "What number is missing in the progression?"
    run_game(rules, generate_round)

if __name__ == "__main__":
    main()