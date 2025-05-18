import re

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

possible_count = 0
for line in lines:
    l1, l2, l3 = map(int, re.findall(r"\d+", line))
    if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
        possible_count += 1

print(possible_count)