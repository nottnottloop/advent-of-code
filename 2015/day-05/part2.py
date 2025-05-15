with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

nice_string_count = 0
#nice_strings = []
for line in lines:
    first_condition = False
    second_condition = False
    # first condition
    pairs = [(i, f"{line[i]}{line[i+1]}") for i in range(len(line) - 1)]

    for first_pair in pairs:
        if first_condition:
            break
        for second_pair in pairs[first_pair[0] + 1:]:
            if second_pair[1] == first_pair[1] and second_pair[0] - first_pair[0] >= 2:
                first_condition = True
                break
    
    # second condition
    trigrams = [f"{line[i]}{line[i+1]}{line[i+2]}" for i in range(len(line) - 2)]
    for trigram in trigrams:
        if trigram[0] == trigram[2]:
            second_condition = True
            break
    
    #print(f"First: {first_condition}")
    #print(f"Second: {second_condition}")
    if first_condition and second_condition:
        #nice_strings.append(line)
        nice_string_count += 1

#for s in nice_strings:
#    print(s)
print(nice_string_count)