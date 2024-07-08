num = 12

abundant_numbers = []

while num <= 28123: # Populate abundant numbers list with every abundant number; constraint set by prob
    sum = 0
    for i in range(1,num): # Find proper divisors and create sum of these
        if num % i == 0:
            sum += i
    if sum > num: # Check if abundant number
        abundant_numbers.append(num)
    num += 1

sums = [] # List of all possible sums of two abundant numbers

for a, abundant_one in enumerate(abundant_numbers): # Find every sum between two abundant numbers
    b = a # Operation always start by summing an abundant number with itself; reduces computation
    while b < len(abundant_numbers): # Nested loop to find sums with num from first loop
        sum = abundant_one + abundant_numbers[b]
        if sum <= 28123: # Constraint implied from problem
            sums.append(sum)
        b += 1

sums_set = set(sums) # Remove duplicates in list of sums

sum = 0
for i in range(1,28123): # Finds sum of all positive integers that are not sums of abundant numbers
    if i not in sums_set: # Membership test
        sum += i

print(sum)
