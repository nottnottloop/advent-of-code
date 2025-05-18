import itertools

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

current_string = lines[0]
for i in range(40):
    new_string = ""
    repeats = [(char, sum(1 for _ in group)) for char, group in itertools.groupby(current_string)]
    for repeat in repeats:
        new_string += f"{repeat[1]}{repeat[0]}"
    current_string = new_string
    #print(current_string)

print(len(current_string))