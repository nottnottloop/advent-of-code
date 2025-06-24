with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

pos = 0
depth = 0
aim = 0

for line in lines:
    instruction, amount = line.split(" ")
    amount = int(amount)
    if instruction == "forward":
        pos += amount
        depth += aim * amount
    elif instruction == "up":
        aim -= amount
    elif instruction == "down":
        aim += amount

print(pos*depth)