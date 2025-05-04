from collections import Counter
import time

t0 = time.time()
with open('input.txt', 'r') as file:
    line = [line.strip() for line in file][0]

stones = line.split(" ")
stones = Counter([int(stone) for stone in stones])

blinks = 75 

def blink_stone(stone):
    stones = Counter()
    if stone == 0:
        stones.update([1])
    elif len(str(stone)) % 2 == 0:
        half_length = len(str(stone)) // 2
        right = int(str(stone)[half_length:])
        left = int(str(stone)[:half_length])
        stones.update([right, left])
    else:
        stones.update([stone*2024])
    return stones

for blinks in range(0, blinks):
    print(f"Blink #{blinks+1}")
    stones = Counter({k:v for k,v in stones.items() if v > 0})
    new_stones = stones.copy()
    stones_to_subtract = Counter()
    for stone, count in stones.items():
        result = blink_stone(stone)
        for new_stone, new_count in result.items():
            new_stones[new_stone] += new_count * count
        stones_to_subtract[stone] = count * -1
    new_stones.update(stones_to_subtract)
    stones = new_stones

print(f"Wow that's {stones.total()} stones")
print(time.time() - t0)
#for e, v in sorted(stones.items()):
#    print(e, v)