import math
import random

from games.engine import run_game


def calculate_lcm(a, b, c):
    lcm_ab = (a * b) // math.gcd(a, b)
    return (lcm_ab * c) // math.gcd(lcm_ab, c)

def generate_round():
    nums = [random.randint(1, 20) for _ in range(3)]
    question = " ".join(map(str, nums))
    answer = calculate_lcm(*nums)
    return question, answer

def main():
    rules = "Find the smallest common multiple of given numbers."
    run_game(rules, generate_round)

if __name__ == "__main__":
    main()