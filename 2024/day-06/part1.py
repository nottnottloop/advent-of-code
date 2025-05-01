with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

map = [[c for c in line] for line in lines]

def print_map():
    print()
    for line in map:
        print(line)

length = len(map)

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
    if x > length - 1 or y > length - 1:
        return "escaped"
    elif map[y][x] == "#":
        return "obstacle"
    elif map[y][x] == ".":
        return "free"

distinct_positions = set()
while True:
    #print_map()
    direction = get_guard_position()
    distinct_positions.add((guard_position[1], guard_position[0]))
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
        
print(len(distinct_positions))