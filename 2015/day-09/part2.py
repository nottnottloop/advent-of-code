import itertools

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]
    
map = {}
named_locations = set()
for line in lines:
    split = line.split(" = ")
    locations, distance = split[0], int(split[1])
    split = locations.split(" to ")
    map[(split[0], split[1])] = distance
    map[(split[1], split[0])] = distance
    named_locations.update([split[0], split[1]])

routes = [perm for perm in itertools.permutations(named_locations)]

#   _____________
#  /             \
# /   THAT'S      \
#|    EASY!       |
#|   _________    |
#|  |  EASY  |    |
#|  | BUTTON |    |
#|  |________|    |
# \             /
#  \___________/
#     \  /
#      \/


longest = 0
for route in routes:
    journeys = list(itertools.pairwise(route))
    result = sum(map[journey] for journey in journeys)
    if result > longest:
        longest = result

print(longest)