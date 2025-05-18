import re

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]
    
current_direction = "n"
x = 0
y = 0

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
    if current_direction == "n":
        y += to_move
    elif current_direction == "e":
        x += to_move
    elif current_direction == "s":
        y -= to_move
    elif current_direction == "w":
        x -= to_move

print(abs(x) + abs(y))