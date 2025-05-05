with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

elves = []
calories = 0
for line in lines:
    if line != "":
        calories += int(line)
    else:
        elves.append(calories)
        calories = 0
        
print(max(elves))