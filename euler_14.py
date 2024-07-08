max_chain = 0
max_num = 0

for num in range (999999,2,-1): # Constraint from problem
    temp = num
    chain_counter = 1  # Counts how many terms are in a chain
    while temp != 1:
        if temp % 2 == 0: # Part of Collatz sequence
            temp /= 2
            chain_counter += 1
        else: # Part of Collatz sequence
            temp = 3 * temp + 1
            chain_counter += 1
    if chain_counter > max_chain: 
        max_chain = chain_counter
        max_num = num

print(max_num)
