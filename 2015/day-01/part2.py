with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

level = 0
for i, c in enumerate(lines[0]):
    if c == "(":
        level += 1
    elif c == ")":
        level -= 1
    if level == -1:
        print(f"Basement: {i + 1}")

print(level)