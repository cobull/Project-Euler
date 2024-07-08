from math import floor,sqrt

triangle_num = 1

while True:
    sum = 0
    for i in range(triangle_num+1): 
        sum += i # Calculate triangle num
    divisors = 2 # All triangle nums have two divisors
    for divisor in range(2,floor(sqrt(sum)+1)): 
        if divisor == sqrt(sum):
            divisors += 1 # If perfect square, only count divisor once
        elif sum % divisor == 0:
            divisors += 2 # Add two to count of divisors since each divisor is paired
    if divisors > 500:
        print(sum)
        break
    triangle_num += 1
