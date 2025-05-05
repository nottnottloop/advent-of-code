# CHRISTMAS TREE!!?!?!?
import math
import re

file_name = "example"
with open(f'{file_name}.txt', 'r') as file:
    lines = [line.strip() for line in file]

if file_name == "example":
    width = 11
    height = 7
else:
    width = 101
    height = 103
    
seconds = 100000
robots = []
# re.findall is better though
re = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")
for line in lines:
    result = re.search(line)
    pos = (int(result[1]), int(result[2]))
    vel = (int(result[3]), int(result[4]))
    robots.append({"pos": pos, "vel": vel})
#robots.append({"pos": (2,4), "vel": (2,-3)})

#print(robots)
def new_robot_position(pos, vel):
    new_x = pos[0] + vel[0]
    new_y = pos[1] + vel[1]
    if new_x < 0:
        new_x = width + new_x
    elif new_x > width - 1:
        new_x = new_x - width
    if new_y < 0:
        new_y = height + new_y
    elif new_y > height - 1:
        new_y = new_y - height
    return (new_x, new_y)

cool_grids = []
for second in range(seconds):
    grid = [[0 for c in range(width)] for c in range(height)]
    for robot in robots:
        robot["pos"] = new_robot_position(robot["pos"], robot["vel"])
        grid[robot["pos"][1]][robot["pos"][0]] += 1
    for row in grid:
        line_count = 0
        for col in row:
            if col == 1:
                line_count += 1
                if line_count == 4:
                    cool_grids.append({"grid": grid, "seconds": second})
            else:
                line_count = 0

for grid in cool_grids:
    print(f"Seconds: {grid["seconds"]}")
    for row in grid["grid"]:
        print(" ".join([str(c) for c in row]))
    print()

print(len(cool_grids))