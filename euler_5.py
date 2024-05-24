x = 20 # Constraint provided by problem

while True:
    is_correct = True
    for i in range(1,21):
        if x % i != 0: # Number must be divisible by all numbers 1-20
            is_correct = False
            break
    if is_correct == True:
        print(x)
        break
    x += 5 # Increment number by 5 since solution must be divisible by 5