amicable_nums = []

num = 1

while num < 10000: # Check all nums under 10000; constraint set by problem
    divisors = []
    for i in range(1,num): # Find and store all proper divisors of num
        if num % i == 0:
            divisors.append(i)
    sum = 0
    for divisor in divisors: # Find the sum of all proper divisors
        sum += divisor
    other_sum = 0
    for j in range(1,sum): # Find proper divisors of sum of proper divisors of num
        if sum % j == 0:
            other_sum += j
    if other_sum == num and sum != num: # Definition of amicable number
        amicable_nums.append(num)
    num += 1

final_sum = 0

for amicable_num in amicable_nums: # Sum of all amicable numbers under 10000
    final_sum += amicable_num

print(final_sum)
