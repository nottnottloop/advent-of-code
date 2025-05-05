with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

map = [[c for c in line] for line in lines]
plots_processed = []
regions = []
map_height = len(map)

def check_surrounding_plots(y, x, region):
    plots_processed.append((y, x))
    neighbour_plots = []
    sides = set()
    for vector in [[-1, 0, "n"], [0, 1, "e"], [1, 0, "s"], [0, -1, "w"]]:
        check_y = y + vector[0]
        check_x = x + vector[1]
        if check_y < 0 or check_y > map_height - 1 or check_x < 0 or check_x > map_height - 1:
            sides.add((check_y, check_x, vector[2]))
            continue
        if map[check_y][check_x] == region["plant"]:
            neighbour_plots.append((check_y, check_x))
        else:
            sides.add((check_y, check_x, vector[2]))
    region["locations"][(y, x)] = {"neighbours": [], "sides": []}
    region["locations"][(y, x)]["neighbours"] = neighbour_plots
    region["locations"][(y, x)]["sides"] = sides
    for neighbour_plot in neighbour_plots:
        if neighbour_plot not in plots_processed:
            check_surrounding_plots(neighbour_plot[0], neighbour_plot[1], region)

for y, row in enumerate(map):
    for x, col in enumerate(row):
        if (y, x) in plots_processed:
            continue

        new_region = {"plant": col, "locations": {}}
        regions.append(new_region)

        check_surrounding_plots(y, x, new_region)

side_to_location_map = {
    'n': ([1, 0]),
    's': ([-1, 0]),
    'e': ([0, -1]),
    'w': ([0, 1]),
}
sum = 0
for region in regions:
    print(region)
    area = len(region["locations"])
    sides = 0
    counted_sides = set()
    shared_sides = set()
    for coords, data in region["locations"].items():
        potential_side_neighbours = set()
        for neighbour in data["neighbours"]:
            for neighbour_side in region["locations"][neighbour]["sides"]:
                for vector in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                    y = neighbour_side[0] + vector[0]
                    x = neighbour_side[1] + vector[1]
                    if not coords == (y, x):
                        potential_side_neighbours.add((y, x, neighbour_side[2]))
        for side in data["sides"]:
            if side in potential_side_neighbours:
                shared_sides.add(side)
        # Add up sides that aren't shared
        sides += len(data["sides"] - shared_sides)
    # Add up sides that are shared
    checked_sides = set()
    shared_sides = list(shared_sides)
    while shared_sides:
        side = shared_sides[0]
        side_to_location_adjustment = side_to_location_map[side[2]]
        if side[2] == 'n' or side[2] == 's':
            vectors = [[0, 1], [0, -1]]
        elif side[2] == 'e' or side[2] == 'w':
            vectors = [[-1, 0], [1, 0]]
        for vector in vectors:
            keep_scanning_this_direction = True
            check_y = side[0]
            check_x = side[1]
            check_y_location = check_y + side_to_location_adjustment[0]
            check_x_location = check_x + side_to_location_adjustment[1]
            while keep_scanning_this_direction:
                check_y += vector[0]
                check_x += vector[1]
                check_y_location += vector[0]
                check_x_location += vector[1]
                if (check_y_location, check_x_location) in region["locations"]:
                    if (check_y, check_x, side[2]) in region["locations"][(check_y_location, check_x_location)]["sides"]:
                        shared_sides.remove((check_y, check_x, side[2]))
                    else:
                        keep_scanning_this_direction = False
                else:
                    keep_scanning_this_direction = False
        shared_sides.remove((side[0], side[1], side[2]))
        sides += 1
    sum += area * sides
    
print(sum)