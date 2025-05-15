filename = "input"

import re
with open(f'{filename}.txt', 'r') as file:
    lines = [line.strip() for line in file]

length = 10 if filename == "example" else 1000
lights = [[False for _ in range(length)] for _ in range(length)]

for line in lines:
    x1, y1, x2, y2 = map(int, re.findall(r"\d+", line))
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            if x >= length or y >= length:
                continue
            if "on" in line:
                lights[y][x] = True
            elif "off" in line:
                lights[y][x] = False
            elif "toggle" in line:
                lights[y][x] = not lights[y][x]

#for y in lights:
#    print(y)
count = sum(cell for row in lights for cell in row)
print(count)