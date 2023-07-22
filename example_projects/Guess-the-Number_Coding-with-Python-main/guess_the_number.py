import random


def generate_random_number(min_num, max_num):
    """Generate a random number between min_num and max_num (inclusive)."""
    return random.randint(min_num, max_num)


def get_random_guess(min_num, max_num):
    """Generate a random guess between min_num and max_num (inclusive)."""
    return random.randint(min_num, max_num)


def check_guess(target, guess):
    """Check if the guess is correct and return 'low', 'high', or 'correct'."""
    if guess < target:
        return "low"
    elif guess > target:
        return "high"
    else:
        return "correct"


def play_guess_the_number():
    """Main function to play the Guess the Number game."""
    min_num = 1
    max_num = 100
    target_number = generate_random_number(min_num, max_num)
    max_attempts = 10
    attempts = 0

    print("Welcome to Guess the Number!")
    print(f"Guess the number between {min_num} and {max_num} (inclusive).")
    print(f"You have {max_attempts} attempts to guess the number.")

    while attempts < max_attempts:
        attempts += 1
        player_guess = get_random_guess(min_num, max_num)

        result = check_guess(target_number, player_guess)

        if result == "correct":
            print(
                f"Congratulations! You guessed the correct number ({target_number}) in {attempts} attempts."
            )
            break
        else:
            print(f"Your guess is too {result}. Try again!")

    if attempts == max_attempts:
        print(
            f"Sorry, you've reached the maximum number of attempts. The correct number was {target_number}."
        )


def main():
    play_guess_the_number()
