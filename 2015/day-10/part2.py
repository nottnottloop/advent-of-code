# putting part 2 bruteforce into a function speeds this up a huge amount to where it doesn't take very long, local variables ftw

import itertools

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

current_string = lines[0]

#print(list(itertools.product(range(1, 4), repeat=2)))

def iterate(s):
    new_string = ""
    repeats = [(char, sum(1 for _ in group)) for char, group in itertools.groupby(s)]
    for repeat in repeats:
        new_string += f"{repeat[1]}{repeat[0]}"
    return new_string

for i in range(50):
    current_string = iterate(current_string)
    print(i)

print(len(current_string))