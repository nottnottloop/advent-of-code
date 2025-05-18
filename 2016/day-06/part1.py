from collections import Counter

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]
    
columns = [Counter() for i in range(len(lines[0]))]
print(columns)

for line in lines:
    for i in range(len(line)):
        columns[i].update(line[i])

print("".join([c.most_common()[0][0] for c in columns]))