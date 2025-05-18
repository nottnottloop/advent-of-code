import re

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

possible_count = 0
sides = []
for line in lines:
    sides.append(int(re.findall(r"\d+", line)[0]))
for line in lines:
    sides.append(int(re.findall(r"\d+", line)[1]))
for line in lines:
    sides.append(int(re.findall(r"\d+", line)[2]))

while sides:
    l3 = sides.pop()
    l2 = sides.pop()
    l1 = sides.pop()
    if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
        possible_count += 1

print(possible_count)