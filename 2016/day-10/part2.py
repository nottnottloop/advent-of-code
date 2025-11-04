import re

filename = "input"
with open(f'{filename}.txt', 'r') as file:
    lines = [line.strip() for line in file]

low_comp = 2 if filename == "example" else 17
high_comp = 5 if filename == "example" else 61

bots = {}
outputs = {}
int_re = re.compile(r"\d+")
transfer_instructions = []

for line in lines:
    if "goes" in line:
        values = list(map(int, re.findall(int_re, line)))
        bots.setdefault(values[1], []).append(values[0])
    else:
        transfer_instructions.append(line)

i = 0
while transfer_instructions:
    if i > len(transfer_instructions) - 1:
        i = 0
    spl = transfer_instructions[i].split(" gives low to ")
    bot_id = int(re.search(int_re, spl[0]).group())
    microchips = sorted(bots.setdefault(bot_id, []))
    if len(microchips) != 2:
        i += 1
        continue

    spl = spl[1].split(" and high to ")
    dest_ids = (int(re.search(int_re, spl[0]).group()), int(re.search(int_re, spl[1]).group()))
    for index, dest_id in enumerate(dest_ids):
        if "output" in spl[index]:
            outputs.setdefault(dest_id, []).append(microchips[index])
        else:
            bots.setdefault(dest_id, []).append(microchips[index])
    transfer_instructions.pop(i)

#print(bots)
print(outputs[0])
print(outputs[1])
print(outputs[2])
print(outputs[0][0] * outputs[1][0] * outputs[2][0])