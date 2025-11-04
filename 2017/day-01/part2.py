with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]
    
for line in lines:
    sum = 0
    next_num = None
    distance = len(line) // 2
    for i in range(len(line)):
        current_num = int(line[i])
        next_num = int(line[(i + distance) % len(line)])
        if current_num == next_num:
            sum += current_num
    print(sum)