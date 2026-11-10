import random
secret_number = random.randint(1, 100)

guess = 0
attempts = 0
range_size = 99
max_attempts = 5

print("=" * 30)
print("Welcome to the Guessing Game!")
print("=" * 30)


while guess != secret_number and attempts < max_attempts:
    guess = int(input(f"Guess a number between 1 and 100: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("=" * 60)
        print(f"Congratulations! You've guessed the secret number {secret_number} in {attempts} attempts.")
        print("Number of attempts:", attempts)
        print("=" * 60)
        break

if guess != secret_number:
    print("=" * 60)
    print(f"Sorry, you've used all {max_attempts} attempts. The secret number was {secret_number}.")
    print("=" * 60)