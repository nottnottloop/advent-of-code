from collections import deque

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

window = deque()
last_sum = None
count = 0

for line in lines:
    window.append(int(line))
    if len(window) < 3:
        continue
    if len(window) == 4:
        window.popleft()
    total = sum(window)
    if last_sum:
        if total > last_sum:
            count += 1
    last_sum = total

print(count)