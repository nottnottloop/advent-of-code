with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

ip_count = 0
for line in lines:
    abas = []
    babs = []
    last_characters = []
    hypernet_sequence = False
    for c in line:
        if c == "[" or c == "]":
            last_characters = []
            if c == "[":
                hypernet_sequence = True
            elif c == "]":
                hypernet_sequence = False
        else:
            last_characters.append(c)
            if len(last_characters) == 4:
                last_characters.pop(0)
            if len(last_characters) == 3:
                if last_characters[0] == last_characters[2] and last_characters[1] != last_characters[0]:
                    if hypernet_sequence:
                        babs.append("".join(last_characters))
                    else:
                        abas.append("".join(last_characters))
    ssl_supported = False
    for aba in abas:
        if ssl_supported:
            break
        for bab in babs:
            if aba[0] == bab[1] and aba[2] == bab[1] and bab[0] == aba[1] and bab[2] == aba[1]:
                if not ssl_supported:
                    ip_count += 1
                    ssl_supported = True
                    break

print(ip_count)