import math
import random
from typing import Tuple

from engine import run_game


def calculate_lcm(a: int, b: int) -> int:
    return a * b // math.gcd(a, b)


def calculate_lcm_of_three(a: int, b: int, c: int) -> int:
    return calculate_lcm(calculate_lcm(a, b), c)


def generate_round() -> Tuple[str, str]:
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    c = random.randint(1, 20)
    question = f"{a} {b} {c}"
    answer = str(calculate_lcm_of_three(a, b, c))
    return question, answer


def play() -> None:
    run_game(
        "Find the smallest common multiple of given numbers.", generate_round
    )
