with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

alphabet = "abcdefghijklmnopqrstuvwxyz"
priorities = {letter:value+1 for value,letter in enumerate(alphabet+alphabet.upper())}

groups = [lines[i:i+3] for i in range(0, len(lines), 3)]

sum = 0
for group in groups:
    group_shared_characters = list(set(group[0]) & set(group[1]) & set(group[2]))
    sum += priorities[group_shared_characters[0]]

print(sum)