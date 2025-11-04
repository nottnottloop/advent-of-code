import re

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]
    
values = []
for line in lines:
    digits = list(map(int, re.findall(r"\d+", line)))
    values.append(max(digits) - min(digits))

print(values)
print(sum(values))