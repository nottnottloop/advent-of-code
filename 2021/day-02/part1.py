with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

pos = 0
depth = 0

for line in lines:
    instruction, amount = line.split(" ")
    amount = int(amount)
    if instruction == "forward":
        pos += amount
    elif instruction == "up":
        depth -= amount
    elif instruction == "down":
        depth += amount

print(pos*depth)