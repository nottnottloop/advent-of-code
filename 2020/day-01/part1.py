with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]
    
numbers = []

for line in lines:
    numbers.append(int(line))

print(numbers)

for i in numbers:
    for j in numbers:
        if i == j:
            continue
        if i + j == 2020:
            print(i * j)
