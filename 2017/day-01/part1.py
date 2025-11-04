with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]
    
for line in lines:
    sum = 0
    last_num = None
    for i in range(len(line) + 1):
        current_num = int(line[i % len(line)])
        if not i == 0:
            last_num = int(line[i % len(line) - 1])
        #print(f"current {current_num}")
        #print(f"last {last_num}")
        if current_num == last_num:
            sum += current_num
    print(sum)