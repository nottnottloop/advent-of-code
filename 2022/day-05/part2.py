import re

filename = "input"
with open(f'{filename}.txt', 'r') as file:
    lines = [line for line in file]
    
stacks = {}
if filename != "example":
    starting_stacks = lines[:9]
    instructions = lines[10:]
else:
    starting_stacks = lines[:4]
    instructions = lines[5:]

for i in range(1, len(starting_stacks[0]), 4):
    stack = []
    for line in starting_stacks:
        if line[i] != " ":
            stack.append(line[i])
    stack_index = stack.pop()
    stacks[stack_index] = list(reversed(stack))
    
for instruction in instructions:
    quantity, origin, destination = re.findall(r"\d+", instruction)
    temp = []
    for i in range(int(quantity)):
        temp.append(stacks[origin].pop())
    for i in range(int(quantity)):
        stacks[destination].append(temp.pop())

message = ""
for stack in stacks.values():
    message += stack[-1]

print(stacks)
print(message)