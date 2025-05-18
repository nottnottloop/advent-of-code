from collections import Counter

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

sum = 0
for line in lines:
    left, right = line.split("[")
    most_common_letters = [right[i] for i in range(0, 5)]
    characters = left.split("-")
    sector_id = int(characters.pop())
    counter = Counter("".join([c for c in characters]))
    real = True
    buffer = []
    counts_seen = []
    while most_common_letters:
        current_highest = counter[most_common_letters[0]]
        if current_highest == 0:
            real = False
            break
        buffer.append(most_common_letters.pop(0))
        while most_common_letters and counter[most_common_letters[0]] == current_highest:
            buffer.append(most_common_letters.pop(0))
        if "".join(buffer) != "".join(sorted(buffer)):
            real = False
            break
        if counts_seen and current_highest > min(counts_seen):
            real = False
            break
        counts_seen.append(current_highest)
        buffer = []

    if real:
        sum += sector_id

print(sum)
