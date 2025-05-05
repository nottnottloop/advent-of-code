import math
import re

file_name = "input"
with open(f'{file_name}.txt', 'r') as file:
    lines = [line.strip() for line in file]

if file_name == "example":
    width = 11
    height = 7
else:
    width = 101
    height = 103
    
seconds = 100
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

for second in range(seconds):
    for robot in robots:
        robot["pos"] = new_robot_position(robot["pos"], robot["vel"])

midpoint_x = width // 2
midpoint_y = height // 2
robots = list(filter(lambda robot: robot["pos"][0] != midpoint_x and robot["pos"][1] != midpoint_y, robots))

robots_in_quadrants = []
quadrant_checks = [
    (range(0, midpoint_x), range(0, midpoint_y)),
    (range(midpoint_x, width), range(0, midpoint_y)),
    (range(0, midpoint_x), range(midpoint_y, height)),
    (range(midpoint_x, width), range(midpoint_y, height)),
]

for quadrant in quadrant_checks:
    robots_in_quadrant = list(filter(lambda robot: robot["pos"][0] in quadrant[0] and robot["pos"][1] in quadrant[1], robots))
    robots_in_quadrants.append(robots_in_quadrant)

print(math.prod([len(quadrant) for quadrant in robots_in_quadrants]))