filename = "input"

import re
with open(f'{filename}.txt', 'r') as file:
    lines = [line.strip() for line in file]

length = 10 if filename == "example" else 1000
lights = [[0 for _ in range(length)] for _ in range(length)]

for line in lines:
    x1, y1, x2, y2 = map(int, re.findall(r"\d+", line))
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            if x >= length or y >= length:
                continue
            if "on" in line:
                lights[y][x] += 1
            elif "off" in line:
                lights[y][x] -= 1
                if lights[y][x] < 0:
                    lights[y][x] = 0
            elif "toggle" in line:
                lights[y][x] += 2

for y in lights:
    print(y)
count = sum(cell for row in lights for cell in row)
print(count)