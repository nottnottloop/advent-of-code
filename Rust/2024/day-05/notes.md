old way

10000000 seeds, follow the path of each one

new way

take for example seed 79 mapping to destination of soil 50. no point in checking seed 80 mapping to 51, because that is a larger number that then maps into the next map

we effectively want the lowest number possible for any given range


# data structures
master garden map: contains the ranges for each map

master garden map: contains the seed ranges

we need to see what different MAP RANGES are valid given SEED RANGES, using the lowest number possible for each seed range

for a given SEED RANGE (one main iteration), map all the possible ranges accessible for each MAP

then, ~~find the highest seed needed~~ (not needed) find the LOWEST location possible

the bottom line: if increasing the source input increases the destination output and doesn't change the next source input range, we shouldn't calculate this

if increasing the source input changes the next source input range, we calculate that




## range mapping
55 in

55 gets mapped to 56

56 then gets mapped to 60

add the differences together