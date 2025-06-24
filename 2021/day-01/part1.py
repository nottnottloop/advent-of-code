with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

last_measurement = None
count = 0

for line in lines:
    measurement = int(line)
    if last_measurement:
        if measurement > last_measurement:
            count += 1
    last_measurement = measurement

print(count)