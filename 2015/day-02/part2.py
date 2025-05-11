import re

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]
    
ribbon_length = 0
for line in lines:
    length, width, height = re.findall(r"\d+", line)
    length, width, height = int(length), int(width), int(height)
    arr = sorted([length, width, height])
    ribbon_length += 2 * arr[0] + 2 * arr[1] + (length*width*height)
    

print(ribbon_length)