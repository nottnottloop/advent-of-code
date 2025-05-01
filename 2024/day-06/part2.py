from copy import deepcopy

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

original_map = [[c for c in line] for line in lines]
map = deepcopy(original_map)

def print_map():
    print()
    for line in map:
        print(line)

length = len(original_map)

guard_position = []
def get_guard_position():
    global guard_position, map
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] != "." and map[y][x] != "#":
                guard_position = [x,y]
                return map[y][x]

get_guard_position()

def check_obstruction(x, y):
    if x > length - 1 or y > length - 1 or x < 0 or y < 0:
        return "escaped"
    elif map[y][x] == "#":
        return "obstacle"
    elif map[y][x] == ".":
        return "free"

time_paradox_counter = 0
time_paradox_tracker = []
def check_time_paradox():
    global time_paradox_tracker
    if not time_paradox_tracker:
        return False
    checked = []
    for t in time_paradox_tracker:
        if t in checked:
            return True
        checked.append(t)
    return False

distinct_positions = set()
while True:
    #print_map()
    direction = get_guard_position()
    distinct_positions.add((guard_position[0], guard_position[1]))
    if direction == "^":
        vector = [0, -1]
    elif direction == ">":
        vector = [1, 0]
    elif direction == "<":
        vector = [-1, 0]
    elif direction == "v":
        vector = [0, 1]
    next_location_type = check_obstruction(guard_position[0] + vector[0], guard_position[1] + vector[1])
    if next_location_type == "escaped":
        break
    if next_location_type == "free":
        map[guard_position[1]][guard_position[0]] = "."
        new_location = [guard_position[0] + vector[0], guard_position[1] + vector[1]]
        map[new_location[1]][new_location[0]] = direction
    elif next_location_type == "obstacle":
        if direction == "^":
            new_direction = ">"
        elif direction == ">":
            new_direction = "v"
        elif direction == "<":
            new_direction = "^"
        elif direction == "v":
            new_direction = "<"
        map[guard_position[1]][guard_position[0]] = new_direction

print(distinct_positions)

for pos_index, distinct_position in enumerate(distinct_positions):
    time_paradox_tracker = []
    map = deepcopy(original_map)
    map[distinct_position[1]][distinct_position[0]] = "#"
    print(f"y: {distinct_position[1]} x: {distinct_position[0]}")
    print(f"You are {round(100 * (pos_index / len(distinct_positions)), 2)}% there")
    while True:
        direction = get_guard_position()
        if check_time_paradox():
            time_paradox_counter += 1
            break
        if direction == "^":
            vector = [0, -1]
        elif direction == ">":
            vector = [1, 0]
        elif direction == "<":
            vector = [-1, 0]
        elif direction == "v":
            vector = [0, 1]
        next_location_type = check_obstruction(guard_position[0] + vector[0], guard_position[1] + vector[1])
        if next_location_type == "escaped":
            break
        if next_location_type == "free":
            map[guard_position[1]][guard_position[0]] = "."
            new_location = [guard_position[0] + vector[0], guard_position[1] + vector[1]]
            map[new_location[1]][new_location[0]] = direction
        elif next_location_type == "obstacle":
            time_paradox_tracker.append((guard_position[1], guard_position[0], direction))
            if direction == "^":
                new_direction = ">"
            elif direction == ">":
                new_direction = "v"
            elif direction == "<":
                new_direction = "^"
            elif direction == "v":
                new_direction = "<"
            map[guard_position[1]][guard_position[0]] = new_direction
        
print(time_paradox_counter)
print(len(distinct_positions))