import collections

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

line = lines[0]
if len(line) < 100:
    print(line)

def create_file_object(length, id):
    return{"id": id, "length": length}

# nah a list won't work
#def return_free_space(blocks):
#    return next((block for block in blocks if block["id"] == -1), None)

#def return_file(blocks):
#    return next((block for block in blocks if block["id"] != -1), None)

decoded_blocks = collections.deque()
compressed_blocks = collections.deque()
for i, c in enumerate(line):
    # File
    if i % 2 == 0:
        decoded_blocks.append(create_file_object(int(c), i//2))
    # Free space
    else:
        decoded_blocks.append(create_file_object(int(c), -1))

print(decoded_blocks)
while decoded_blocks:
    next_block = decoded_blocks[0]
    last_block = decoded_blocks[-1]
    if next_block["id"] != -1:
        compressed_blocks.append(decoded_blocks.popleft())
    else:
        if last_block["length"] < next_block["length"]:
            next_block["length"] -= last_block["length"]
            compressed_blocks.append(decoded_blocks.pop())
            last_block = decoded_blocks[-1]
        else:
            last_block["length"] -= next_block["length"]
            next_block["id"] = last_block["id"]
    while decoded_blocks:
        if next_block["length"] == 0:
            decoded_blocks.popleft()
            if decoded_blocks:
                next_block = decoded_blocks[0]
        if last_block["id"] == -1 or last_block["length"] == 0:
            decoded_blocks.pop()
            if decoded_blocks:
                last_block = decoded_blocks[-1]
        else:
            break

if compressed_blocks[-1]["id"] == compressed_blocks[-2]["id"]:
    compressed_blocks[-2]["length"] += compressed_blocks.pop()["length"]
    
total_length = sum(block["length"] for block in compressed_blocks)

checksum = 0
for index in range(total_length):
    checksum += compressed_blocks[0]["id"] * index
    compressed_blocks[0]["length"] -= 1
    if compressed_blocks[0]["length"] == 0:
        compressed_blocks.popleft()

print(decoded_blocks)
print(compressed_blocks)
print(checksum)
#print(next_free_space)
#print(last_file)