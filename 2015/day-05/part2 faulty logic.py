with open('example.txt', 'r') as file:
    lines = [line.strip() for line in file]

nice_string_count = 0
for line in lines:
    first_condition = False
    second_condition = False
    # first condition
    pairs = []
    for i in range(len(line) - 1):
        pairs.append((i, f"{line[i]}{line[i+1]}"))
    for pair in pairs:
        overlapping = True
        if first_condition:
            break
        for second_pair in pairs[pair[0] + 1:]:
            if second_pair[1] != pair[1]:
                overlapping = False
            elif second_pair[1] == pair[1] and not overlapping:
                first_condition = True
                break
    trigrams = []
    # second condition
    for i in range(len(line) - 2):
        trigrams.append(f"{line[i]}{line[i+1]}{line[i+2]}")
    for trigram in trigrams:
        if trigram[0] == trigram[2]:
            second_condition = True
            break
    
    print(f"First: {first_condition}")
    print(f"Second: {second_condition}")
    if first_condition and second_condition:
        nice_string_count += 1

print(nice_string_count)