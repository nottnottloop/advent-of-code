# range theory

1. no overlapping
2. destination range of first map is completely within source range of second map
3. destination range of first map partially overlapping: starting lower than second map source range and finishing inside second map source range
4. or destination range of first map beginning inside second map source range and ending outside of second map source range

in the case of no overlapping or partial overlapping, **maintain** the original transformation when folding the maps

# overlapping
e.g.

2..5
6..8
range1.start < range2.end && range2.start < range1.end
no

2..5
1..2
range1.start < range2.end && range2.start < range1.end
no

2..5
4..6
range1.start < range2.end && range2.start < range1.end
yes