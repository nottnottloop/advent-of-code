with open(f'input.txt', 'r') as file:
    line = [line.strip() for line in file][0]

for i, c in enumerate(line):
    characters = set(line[i:i+14])
    if len(characters) == 14:
        print(i + 14)
        break