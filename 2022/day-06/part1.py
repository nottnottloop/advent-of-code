with open(f'input.txt', 'r') as file:
    line = [line.strip() for line in file][0]

for i, c in enumerate(line):
    characters = set(line[i:i+4])
    if len(characters) == 4:
        print(i + 4)
        break