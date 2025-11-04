import re

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]
    
values = []
for line in lines:
    digits = list(map(int, re.findall(r"\d+", line)))
    value_found = False
    if not value_found:
        for d1 in digits:
            for d2 in digits:        
                if d1 // d2 == d1 / d2 and d1 != d2:
                    values.append(d1 // d2)
                    value_found = True
                    break
    print(values)

print(sum(values))