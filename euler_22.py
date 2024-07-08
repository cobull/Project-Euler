import re

with open("names.txt") as f:
    data = f.read()

p = re.compile(r'\w+') # Regex to match only the names

word_list = p.findall(data) # Finds all occurences of "names" in the data and stores in a list

sorted_list = sorted(word_list,key=str.casefold) # Sorts the names in the list, alphabetical

total_sum = 0

for index,name in enumerate(sorted_list): # Find total of name scores as directed by problem
    sum = 0
    for char in name: 
        sum = sum + (ord(char) - 64)
    total_sum = total_sum + sum * (index + 1)

print(total_sum)
