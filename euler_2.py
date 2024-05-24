a = 1 # First fibo number
b = 2 # Second fibo number

sum = 0

while b <= 4000000: # Constraint from problem
    if b % 2 == 0:
        sum += b # Sum of all even fibo numbers
    temp = b
    b = a + b
    a = temp

print(sum)