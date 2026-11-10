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