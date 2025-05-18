with open('input.txt', 'r') as file:
    line = [line.strip() for line in file][0]

decompressed = ""
i = 0
while i < len(line):
    if line[i] != "(":
        decompressed += line[i]
        i += 1
    else:
        look_ahead_str = ""
        while True:
            i += 1
            if line[i].isdigit():
                look_ahead_str += line[i]
            else:
                break
        look_ahead = int(look_ahead_str)
        repeats_str = ""
        while True:
            i += 1
            if line[i].isdigit():
                repeats_str += line[i]
            else:
                break
        repeats = int(repeats_str)
        sequence = ""
        for j in range(1, look_ahead + 1):
            sequence += line[i+j]
        decompressed += sequence * repeats
        i += look_ahead + 1


print(decompressed)
print(len(decompressed))