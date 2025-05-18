with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

ip_count = 0
for line in lines:
    last_characters = []
    hypernet_sequence = False
    abba = False
    abba_in_hypernet_sequence = False
    for c in line:
        if c == "[" or c == "]":
            last_characters = []
            if c == "[":
                hypernet_sequence = True
            elif c == "]":
                hypernet_sequence = False
        else:
            last_characters.append(c)
            if len(last_characters) == 5:
                last_characters.pop(0)
            if len(last_characters) == 4:
                if last_characters[0:2] == list(reversed(last_characters[2:4])) and last_characters[0] != last_characters[1]:
                    if hypernet_sequence:
                        abba_in_hypernet_sequence = True
                        break
                    abba = True
    if abba and not abba_in_hypernet_sequence:
        ip_count += 1

print(ip_count)