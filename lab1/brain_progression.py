import random
from typing import List, Tuple

from engine import run_game


def generate_progression(start: int, step: int, length: int) -> List[int]:
    return [start * (step**i) for i in range(length)]


def generate_round() -> Tuple[str, str]:
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    step = random.randint(2, 5)
    hidden_index = random.randint(0, length - 1)

    progression = generate_progression(start, step, length)
    answer = str(progression[hidden_index])
    progression[hidden_index] = ".."
    question = " ".join(map(str, progression))

    return question, answer


def play() -> None:
    run_game("What number is missing in the progression?", generate_round)
