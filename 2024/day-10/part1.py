with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

map = [[c for c in line] for line in lines]

trailhead_locations = {}
for i, row in enumerate(map):
    for j, col in enumerate(row):
        if col == "0":
            trailhead_locations[(i, j)] = set()

height = len(map[0])

def follow(y, x, current_height, original_trailhead):
    global counter
    #print(f"{y}, {x}")
    for vector in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        check_y = y + vector[0]
        check_x = x + vector[1]
        if check_y >= 0 and check_y < height and check_x >= 0 and check_x < height:
            check_tile = map[check_y][check_x]
            if check_tile == ".":
                continue
            check_height = int(check_tile)
            if check_height == current_height + 1:
                if check_height == 9:
                    trailhead_locations[original_trailhead].add((check_y, check_x))
                else:
                    follow(check_y, check_x, check_height, original_trailhead)

for trailhead in trailhead_locations.keys():
    follow(trailhead[0], trailhead[1], 0, trailhead)
    
summit_count = 0
for summits in trailhead_locations.values():
    summit_count += len(summits)

print(summit_count)
    
#print(trailhead_locations)
#for line in map:
#    print(" ".join(line))