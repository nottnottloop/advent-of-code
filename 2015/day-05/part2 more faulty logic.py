with open('example.txt', 'r') as file:
    lines = [line.strip() for line in file]

def check_overlap(i):
    global too_long
    result = False
    for range in too_long:
        if i >= range.start and i < range.stop:
            result = True
    return result

too_long = []
nice_string_count = 0
nice_strings = []
for line in lines:
    first_condition = False
    second_condition = False
    # first condition
    pairs = []
    for i in range(len(line) - 1):
        pairs.append((i, f"{line[i]}{line[i+1]}"))

    check_char = line[0]
    start = 0
    counter = 1
    for i in range(1, len(line)):
        if check_char == line[i]:
            counter += 1
        if counter >= 3:
            too_long.append(range(start,start+counter))
        if check_char != line[i]:
            counter = 1
            start = i
            check_char = line[i]

    for pair in pairs:
        if first_condition:
            break
        if check_overlap(pair[0]):
            continue
        for second_pair in pairs[pair[0] + 1:]:
            if check_overlap(second_pair[0]):
                continue
            if second_pair[1] == pair[1]:
                first_condition = True
                break
    
    too_long = []
    # second condition
    trigrams = []
    for i in range(len(line) - 2):
        trigrams.append(f"{line[i]}{line[i+1]}{line[i+2]}")
    for trigram in trigrams:
        if trigram[0] == trigram[2]:
            second_condition = True
            break
    
    print(f"First: {first_condition}")
    print(f"Second: {second_condition}")
    if first_condition and second_condition:
        nice_strings.append(line)
        nice_string_count += 1

for s in nice_strings:
    print(s)
print(nice_string_count)