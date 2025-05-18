with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]
    
x = 0
y = 2
map = [
    ["", "", "1", "", ""],
    ["", "2", "3", "4", ""],
    ["5", "6", "7", "8", "9"],
    ["", "A", "B", "C", ""],
    ["", "", "D", "", ""],
]

def move(direction):
    global x, y
    temp_x, temp_y = x, y
    if direction == "U":
        temp_y -= 1
    elif direction == "L":
        temp_x -= 1
    elif direction == "R":
        temp_x += 1
    elif direction == "D":
        temp_y += 1
    if temp_x < 0:
        temp_x = 0
    if temp_y < 0:
        temp_y = 0
    if temp_x > 4:
        temp_x = 4
    if temp_y > 4:
        temp_y = 4
    if map[temp_y][temp_x]:
        x, y = temp_x, temp_y

code = ""
for line in lines:
    for direction in line:
        move(direction)
    code += str(map[y][x])
    
print(code)