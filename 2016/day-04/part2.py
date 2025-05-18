import string
from collections import Counter

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]


def decrypt_room_name(room_string):
    words = room_string.split("-")
    sector_id = int(words.pop())
    decrypted = ""
    for c in "".join(words):
        decrypted += string.ascii_lowercase[(sector_id + string.ascii_lowercase.find(c)) % 26]
    return f"{decrypted} {sector_id}"

real_rooms = []
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
        real_rooms.append(left)

for room in real_rooms:
    name = decrypt_room_name(room)
    if "pole" in name:
        print(name)