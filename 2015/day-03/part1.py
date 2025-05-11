from collections import Counter

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

locations_visited = Counter()
x = 0
y = 0
locations_visited[(x, y)] = locations_visited.get((x, y), 0) + 1
for c in lines[0]:
    if c == ">":
        x += 1
    elif c == "<":
        x -= 1
    elif c == "^":
        y += 1
    elif c == "v":
        y -= 1
    locations_visited[(x, y)] = locations_visited.get((x, y), 0) + 1
    
print(len(locations_visited))