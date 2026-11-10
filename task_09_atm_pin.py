print("="*40)
print("Welcome to the ATM")
print("="*40)

atm_pin = "1234"
attempts = 0
max_attempt = 3

while attempts < max_attempt:
      guessed_pin = input("Enter A 4-digit PIN: ").strip()

      if not guessed_pin.isdigit():
          print("⚠️ PIN must contain only digits. Try again.\n")
          continue

      if len(guessed_pin) != 4:
          print(f"⚠️ PIN must be exactly 4 digits. You entered {len(guessed_pin)}.\n")
          continue  
      if guessed_pin == atm_pin:
       print("Correct PIN. Access granted.")
       break