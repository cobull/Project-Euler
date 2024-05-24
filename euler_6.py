squares = [x**2 for x in range(1,101)] # List of squared numbers

sum_of_squares = 0
for square in squares:
    sum_of_squares += square

sum = 0
for num in range(1,101):
    sum += num

square_of_sum = sum**2

print(square_of_sum - sum_of_squares)