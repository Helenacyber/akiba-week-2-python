print("="*40)
print("Welcome to the ATM")
print("="*40)

atm_pin = "1234"
attempts = 0
max_attempt = 3

while attempts < max_attempt:
      guessed_pin = input("Enter A 4-digit PIN: ").strip()