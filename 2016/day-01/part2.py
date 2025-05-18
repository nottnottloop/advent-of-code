import re

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]
    
current_direction = "n"
x = 0
y = 0

locations_visited = []

def get_new_direction(turn):
    global current_direction
    left_or_right = 0 if turn == "L" else 1
    if current_direction == "n":
        current_direction = ["w", "e"][left_or_right]
    elif current_direction == "e":
        current_direction = ["n", "s"][left_or_right]
    elif current_direction == "s":
        current_direction = ["e", "w"][left_or_right]
    elif current_direction == "w":
        current_direction = ["s", "n"][left_or_right]

for instruction in lines[0].split(", "):
    to_move = int(re.findall(r"\d+", instruction)[0])
    get_new_direction(instruction[0])
    while to_move != 0:
        if current_direction == "n":
            y += 1
        elif current_direction == "e":
            x += 1
        elif current_direction == "s":
            y -= 1
        elif current_direction == "w":
            x -= 1
        if (x, y) in locations_visited:
            print(f"Easter Bunny Headquarters: {(abs(x) + abs(y))}")
            break
        else:
            locations_visited.append((x, y))
        to_move -= 1