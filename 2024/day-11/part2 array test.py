import array
import sys
import pympler.asizeof

with open('input.txt', 'r') as file:
    line = [line.strip() for line in file][0]

array_data_type = "I"
og_stones = line.split(" ")
#og_stones = [int(stone) for stone in og_stones]
og_stones = array.array(array_data_type, [int(stone) for stone in og_stones])

blinks = 25
blink_step = 5 
cache = {}

def blink_stone_multiple_times(stone):
    if stone not in cache:
        stones = array.array(array_data_type, [stone])
        for blink in range(blink_step):
            i = 0
            while i < len(stones):
                if stones[i] == 0:
                    stones[i] = 1
                elif len(str(stones[i])) % 2 == 0:
                    half_length = len(str(stones[i])) // 2
                    right = int(str(stones[i])[half_length:])
                    left = int(str(stones[i])[:half_length])
                    stones.pop(i)
                    stones.insert(i, right)
                    stones.insert(i, left)
                    i += 1
                else:
                    stones[i] *= 2024
                i += 1
        cache[stone] = stones
    return cache[stone]

for blinks in range(0, blinks, blink_step):
    print(f"Blinks: {blinks}")
    new_stones = array.array(array_data_type, [])
    for og_stone in range(len(og_stones)):
        new_stones.extend(blink_stone_multiple_times(og_stones[og_stone]))
    og_stones = new_stones
        #print(f"Blink: {blink} Stones: {len(stones)}")

#print(stones)
#total_stones = sum(len(stones) for stones in og_stones)
print(f"Array size: {pympler.asizeof.asizeof(og_stones)/1000}kb")
total_stones = len(og_stones)
print(f"Wow that's {total_stones} stones")