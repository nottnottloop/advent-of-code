from collections import Counter

with open('example.txt', 'r') as file:
    line = [line.strip() for line in file][0]

stones = line.split(" ")
stones = [int(stone) for stone in stones]

blinks = 10

for blink in range(blinks):
    i = 0
    while i < len(stones):
        if stones[i] == 0:
            stones[i] = 1
        elif len(str(stones[i])) % 2 == 0:
            half_length = len(str(stones[i])) // 2
            right = int(str(stones[i])[half_length:])
            left = int(str(stones[i])[:half_length])
            if left == 94:
                print(stones[i])
                print(left)
            if right == 94:
                print(stones[i])
                print(right)
            stones.pop(i)
            stones.insert(i, right)
            stones.insert(i, left)
            i += 1
        else:
            stones[i] *= 2024
        i += 1
    #print(len(stones))

new_counter = Counter(stones)
print(f"Wow that's {new_counter.total()} stones")
#for e, v in sorted(new_counter.items()):
#    print(e, v)