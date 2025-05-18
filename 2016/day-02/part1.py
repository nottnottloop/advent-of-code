with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]
    
x = 1
y = 1
map = {
    (0, 0): 1,
    (1, 0): 2,
    (2, 0): 3,
    (0, 1): 4,
    (1, 1): 5,
    (2, 1): 6,
    (0, 2): 7,
    (1, 2): 8,
    (2, 2): 9,
}

code = ""
for line in lines:
    for direction in line:
        if direction == "U":
            y -= 1
        elif direction == "L":
            x -= 1
        elif direction == "R":
            x += 1
        elif direction == "D":
            y += 1
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        if x > 2:
            x = 2
        if y > 2:
            y = 2
    code += str(map[(x, y)])
    
print(code)