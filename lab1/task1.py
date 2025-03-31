import random


def gcd(a, b):
    """Calculates GCD of two numbers."""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Calculates LCM of two numbers."""
    return a * b // gcd(a, b)


def lcm_three(a, b, c):
    """Calculates LCM of three numbers."""
    return lcm(lcm(a, b), c)


def generate_numbers():
    """Generates three random numbers."""
    return [random.randint(1, 100) for _ in range(3)]


def play_game():
    """Plays the LCM game."""
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the smallest common multiple of given numbers.\n")

    correct_answers = 0
    total_questions = 3

    for _ in range(total_questions):
        numbers = generate_numbers()
        correct_answer = lcm_three(*numbers)
        print(f"Question: {' '.join(map(str, numbers))}")
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


if __name__ == "__main__":
    play_game()