num = str(2**1000) # Turning number in question into iterable object

sum = 0
for char in num: # Iterating through each digit in number and adding to sum
    digit = int(char)
    sum += digit

print(sum)
