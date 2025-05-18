import re

filename = "input"
with open(f'{filename}.txt', 'r') as file:
    lines = [line.strip() for line in file]

height = 6 if filename != "example" else 3
width = 50 if filename != "example" else 7

screen = [["." for _ in range(width)] for _ in range(height)]

for line in lines:
    numbers = list(map(int, re.findall(r"\d+", line)))
    if "rect" in line:
        for y in range(numbers[1]):
            for x in range(numbers[0]):
                screen[y][x] = "#"
    elif "rotate column" in line:
        for i in range(numbers[1]):
            last_pixel = screen[-1][numbers[0]]
            for y in range(height):
                new_last_pixel = screen[y][numbers[0]]
                screen[y][numbers[0]] = last_pixel
                last_pixel = new_last_pixel
    elif "rotate row" in line:
        for i in range(numbers[1]):
            last_pixel = screen[numbers[0]][-1]
            for x in range(width):
                new_last_pixel = screen[numbers[0]][x]
                screen[numbers[0]][x] = last_pixel
                last_pixel = new_last_pixel
            

for m in screen:
    print(" ".join(m))

print(sum([sum([1 for i in r if i == "#"]) for r in screen]))

# or

print(sum(row.count("#") for row in screen))

# lol part 2 solves itself