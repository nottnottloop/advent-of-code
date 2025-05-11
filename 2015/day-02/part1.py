import re

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]
    
total_wrapping_paper = 0
for line in lines:
    length, width, height = re.findall(r"\d+", line)
    length, width, height = int(length), int(width), int(height)
    part1 = length * width
    part2 = width * height
    part3 = height * length
    total_wrapping_paper += 2 * part1 + 2 * part2 + 2 * part3 + min([part1, part2, part3])

print(total_wrapping_paper)