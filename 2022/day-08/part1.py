with open(f'input.txt', 'r') as file:
    lines = [line.strip() for line in file]

map = [[int(c) for c in line] for line in lines]
length = len(map)

visible_count = (len(map[0]) * 2) + ((len(map[0]) - 2) * 2)
print(visible_count)
for y in range(1, len(map) - 1):
    for x in range(1, len(map[0]) - 1):
        visible = False
        tree_height = map[y][x]
        for vector in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            if visible:
                break
            check_y = y
            check_x = x
            while True:
                check_y += vector[0]
                check_x += vector[1]
                if check_y < 0 or check_y > length - 1 or check_x < 0 or check_x > length - 1:
                    visible = True
                    break
                if not map[check_y][check_x] < tree_height:
                    break
        if visible:
            visible_count += 1


for m in map:
    print(m)
    
print(visible_count)