def fibo(a,b): 
    """
    Function that calculates the next fibonacci number.

    Parameters
        a: first previous fibonacci number of the one being calculated
        b: second previous fibonacci number of the one being calculated

    Returns
        next_term: the next fibonacci number
    """ 
    next_term = a + b
    return next_term

def digit_count(num):
    """
    Function that calculates the number of digits of a number.

    Parameters
        num: the number whose digits will be calculated

    Returns
        num_digits: the number of digits in num
    """ 
    num_digits = 0
    num = str(num)
    for digit in num:
        num_digits += 1
    return num_digits

n = 3
a = 1 # Second fibonacci number
b = 1 # First fibonacci number

while True: # Finds the next fibo number, calculates the digits, and loops until digits equal 1000
    next_term = fibo(a,b)
    if digit_count(next_term) == 1000:
        break
    b = a
    a = next_term
    n += 1

print(n)
