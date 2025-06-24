with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

gamma_rate = ""
epsilon_rate = ""
data = [[] for _ in range(len(lines[0]))]

for line in lines:
    for i, c in enumerate(line):
        data[i].append(c)

for col in data:
    ones = 0
    zeros = 0
    for c in col:
        if c == "0":
            zeros += 1
        elif c == "1":
            ones += 1
    if ones > zeros:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)
print(gamma_rate)
print(epsilon_rate)

print(gamma_rate * epsilon_rate)