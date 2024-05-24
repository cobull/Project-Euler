
max_palindrome = 0 

for a in range(999,99,-1):
    for b in range(999,99,-1):
        c = a * b 
        digits = [int(digit) for digit in str(c)] # List of individual digits of the product
        if digits == digits[::-1] and max_palindrome < c: # Checks if list and reversed list is the same (palindrome)
            max_palindrome = c

print(max_palindrome)