multiples = [x for x in range(1,1000) if x % 3 == 0 or x % 5 == 0] # Create list of all multiples

sum = 0 

for multiple in multiples:
    sum += multiple

print(sum)