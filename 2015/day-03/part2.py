from collections import Counter

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

locations_visited = Counter()
santa = [0, 0]
robo_santa = [0, 0]
locations_visited[(0, 0)] = locations_visited.get((0, 0), 0) + 1
for i, c in enumerate(lines[0]):
    current_santa = santa if i % 2 == 0 else robo_santa
    if c == ">":
        current_santa[0] += 1
    elif c == "<":
        current_santa[0] -= 1
    elif c == "^":
        current_santa[1] += 1
    elif c == "v":
        current_santa[1] -= 1
    locations_visited[(current_santa[0], current_santa[1])] = locations_visited.get((current_santa[0], current_santa[1]), 0) + 1
    
print(len(locations_visited))