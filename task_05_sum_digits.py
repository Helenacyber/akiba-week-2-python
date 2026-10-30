# Task 5: Sum of Digits
number = int(input("Enter a number: "))
number = abs(number)  # Handle negative numbers
total = 0

while number > 0:
    digit = number % 10
    total += digit
    number = number // 10

print("Sum of digits:", total)