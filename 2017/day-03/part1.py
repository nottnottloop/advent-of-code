with open('example.txt', 'r') as file:
    lines = [line.strip() for line in file]

for line in lines:
    square = int(line)
    for i in range(square):
        print(i)
    break