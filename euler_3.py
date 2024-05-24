from math import sqrt, floor

x = floor(sqrt(600851475143)) # Factors can't be greater than this number

factors = [y for y in range(2,x) if 600851475143 % y == 0] # List of all factors

factors = factors[::-1] # Reverse list so that the largest factor is first

for factor in factors: 
    is_prime = True
    for x in range(2,floor(sqrt(factor))):
        if factor % x == 0:
            is_prime = False
            break # If number is divisible by another number then break from for loop
    if is_prime == True: # Only a prime factor will enter this conditional
        print(factor)
        break # No need to check rest of factors