from math import sqrt, floor

number = 13 # Number in question, 13 is the sixth prime number
i = 6 # Prime number counter, 13 is the sixth prime number

number += 1
while i < 10001:
    is_prime = True
    for x in range(2,floor(sqrt(number)) + 1):
        if number % x == 0:
            is_prime = False
            break # No need to keep checking if number is prime if it's divisible by another
    if is_prime:
        i += 1 # Increment prime number counter if number is prime number
    if i == 10001:
        break
    number += 1 # Increment number to test

print(number)