product = 1

num = 100

while num >= 1: # Calculating factorial 100
    product *= num
    num -= 1

product = str(product) # Turning factorial into iterable object

sum = 0
for digit in product: # Iterating through number and adding each digit to sum
    digit = int(digit)
    sum += digit

print(sum)
