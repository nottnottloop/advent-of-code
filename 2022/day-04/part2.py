import re

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

pairs = []
for line in lines:
    section_assignments = re.findall(r"\d+", line)
    section_assignments = [int(i) for i in section_assignments]
    pairs.append((range(section_assignments[0], section_assignments[1]), range(section_assignments[2], section_assignments[3])))
    
def is_overlapping(range1: range, range2: range):
    #return range1.stop >= range2.start or range1.start <= range2.stop
    return not (range1.stop < range2.start or range2.stop < range1.start)

overlapping_ranges_count = 0
print(pairs)
for pair in pairs:
    if is_overlapping(pair[0], pair[1]) or is_overlapping(pair[1], pair[0]):
        overlapping_ranges_count += 1
        
print(overlapping_ranges_count)