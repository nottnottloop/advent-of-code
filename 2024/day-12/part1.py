with open('example.txt', 'r') as file:
    lines = [line.strip() for line in file]

map = [[c for c in line] for line in lines]
plots_processed = []
regions = []

map_height = len(map)

def check_surrounding_plots(y, x, region):
    plots_processed.append((y, x))
    neighbour_plots = []
    for vector in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        check_y = y + vector[0]
        check_x = x + vector[1]
        if check_y < 0 or check_y > map_height - 1 or check_x < 0 or check_x > map_height - 1:
            continue
        if map[check_y][check_x] == region["plant"]:
            neighbour_plots.append((check_y, check_x))
    region["locations"][(y, x)] = neighbour_plots
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

sum = 0
for region in regions:
    print(region)
    area = len(region["locations"])
    perimeter = 0
    for location, neighbours in region["locations"].items():
        perimeter += 4 - len(neighbours)
    sum += area * perimeter
    
print(sum)
    
    