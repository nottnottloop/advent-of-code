with open('myexample2.txt', 'r') as file:
    line = [line.strip() for line in file][0]

stones = line.split(" ")
stones = [int(stone) for stone in stones]

blinks = 10 

for stone in stones:
    this_stone = [stone]
    for blink in range(blinks):
        i = 0
        while i < len(this_stone):
            if this_stone[i] == 0:
                this_stone[i] = 1
            elif len(str(this_stone[i])) % 2 == 0:
                half_length = len(str(this_stone[i])) // 2
                right = int(str(this_stone[i])[half_length:])
                left = int(str(this_stone[i])[:half_length])
                this_stone.pop(i)
                this_stone.insert(i, right)
                this_stone.insert(i, left)
                i += 1
            else:
                this_stone[i] *= 2024
            i += 1
        #print(len(stones))

    #print(stones)
    print(f"Wow that's {len(this_stone)} stones")