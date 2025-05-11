with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

level = 0
for c in lines[0]:
    if c == "(":
        level += 1
    elif c == ")":
        level -= 1

print(level)