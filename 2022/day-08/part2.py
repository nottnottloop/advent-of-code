import math

with open(f'input.txt', 'r') as file:
    lines = [line.strip() for line in file]

map = [[int(c) for c in line] for line in lines]
length = len(map)

all_scenic_scores = []
visible_count = (len(map[0]) * 2) + ((len(map[0]) - 2) * 2)
for y in range(1, len(map) - 1):
    for x in range(1, len(map[0]) - 1):
        tree_height = map[y][x]
        scenic_scores = []
        for vector in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            scenic_score = 0
            check_y = y
            check_x = x
            while True:
                check_y += vector[0]
                check_x += vector[1]
                if check_y < 0 or check_y > length - 1 or check_x < 0 or check_x > length - 1:
                    break
                scenic_score += 1
                if not map[check_y][check_x] < tree_height:
                    break
            scenic_scores.append(scenic_score)
        all_scenic_scores.append(math.prod(scenic_scores))

print(all_scenic_scores)
print(max(all_scenic_scores))
#for m in map:
#    print(m)