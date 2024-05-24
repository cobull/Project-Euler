from math import sqrt, floor

def is_prime(number):
    """
    Function that tests whether a number is a prime number

    Parameter
        number: and integer to be tested for prime property

    Returns
        True if number is prime
        False if number is not prime
    """
    for x in range(1,floor(sqrt(number)) + 1):
        if number % x == 0 and x != 1:
            return False 
    return True

primes = [number for number in range(2,2000000) if is_prime(number)] # Build list of prime nums

sum = 0

for prime in primes:
    sum += prime

print(sum)