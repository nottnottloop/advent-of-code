import itertools

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

antenna_map = [[c for c in line] for line in lines]
antenna_types = set()
for row in antenna_map:
    for col in row:
        if col != ".":
            antenna_types.add(col)

length = len(antenna_map)
#antinode_map = [['.'] * length for _ in range(length)]
antinode_map = [['.' for i in range(length)] for j in range(length)]

for antenna_type in antenna_types:
    antenna_locations = []
    for row_index, row in enumerate(antenna_map):
        for col_index, col in enumerate(row):
            if col == antenna_type:
                antenna_locations.append((row_index, col_index))
    atenna_permutations = list(itertools.permutations(antenna_locations, 2))
    print(antenna_type)
    for atenna_permutation in atenna_permutations:
        inverse_vector = ((atenna_permutation[1][0] - atenna_permutation[0][0]) * -1, (atenna_permutation[1][1]-atenna_permutation[0][1]) * -1)
        antinode_location = (atenna_permutation[0][0] + inverse_vector[0], atenna_permutation[0][1] + inverse_vector[1])
        print(antinode_location)
        if antinode_location[0] < length and antinode_location[0] >= 0 and antinode_location[1] < length and antinode_location[1] >= 0:
            antinode_map[antinode_location[0]][antinode_location[1]] = antenna_type

antinode_count = 0
for row in antinode_map:
    for col in row:
        if col != ".":
            antinode_count += 1

#print(antenna_types)
for line in antinode_map:
    print(line)
print(antinode_count)