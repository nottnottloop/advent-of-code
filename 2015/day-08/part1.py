with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

raw_count = 0
parsed_count = 0
for line in lines:
    raw_count += len(line)
    parsed_count += len(eval(line))

print(raw_count - parsed_count)