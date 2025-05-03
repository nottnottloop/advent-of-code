with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

line = lines[0]
#if len(line) < 100:
#    print(line)

def create_file_object(length, id):
    return{"id": id, "length": length}

# oh i guess lists were fine the entire time
decoded_blocks = []
#compressed_blocks = []
for i, c in enumerate(line):
    if c == "0":
        continue
    # File
    if i % 2 == 0:
        decoded_blocks.append(create_file_object(int(c), i//2))
    # Free space
    else:
        decoded_blocks.append(create_file_object(int(c), "free"))

start_free_space_search_index = 0
start_file_search_index = len(decoded_blocks) - 1
#free_id = 0
while True:
    if start_free_space_search_index > start_file_search_index:
        break
    for i in range(start_free_space_search_index, len(decoded_blocks)):
        if decoded_blocks[i]["id"] == "free":
            next_free_space = decoded_blocks[i]
            start_free_space_search_index = i
            break
    for i in range(start_file_search_index, 0, -1):
        if decoded_blocks[i]["id"] != "free":
            next_file = decoded_blocks[i]
            start_file_search_index = i
            break
    for i in range(start_free_space_search_index, start_file_search_index):
        if decoded_blocks[i]["id"] == "free" and decoded_blocks[i]["length"] >= next_file["length"]:
            remaining_length = decoded_blocks[i]["length"] - next_file["length"]
            decoded_blocks[i]["id"] = next_file["id"]
            decoded_blocks[i]["length"] = next_file["length"]
            if remaining_length > 0:
                decoded_blocks.insert(i+1, create_file_object(remaining_length, "free"))
                start_file_search_index += 1
            next_file["id"] = "free"
            break
    # Clump free space around free space that was just opened up into just one object
    # start_file_search_index and next_file is now the original empty space
    total_extra_free_spaces = 0
    counter = 1
    #print(start_file_search_index)
    if decoded_blocks[start_file_search_index]["id"] == "free":
        while True:
            if start_file_search_index + counter < len(decoded_blocks)  and decoded_blocks[start_file_search_index+counter]["id"] == "free":
                total_extra_free_spaces += decoded_blocks[start_file_search_index+counter]["length"]
                decoded_blocks[start_file_search_index+counter]["length"] = 0
                counter += 1
            else:
                break
        counter = 1
        while True:
            if decoded_blocks[start_file_search_index-counter]["id"] == "free":
                total_extra_free_spaces += decoded_blocks[start_file_search_index-counter]["length"]
                decoded_blocks[start_file_search_index-counter]["length"] = 0
                counter += 1
            else:
                break
        next_file["length"] += total_extra_free_spaces
        #next_file["lol"] = free_id
        #free_id += 1
    start_file_search_index -= 1

#if compressed_blocks[-1]["id"] == compressed_blocks[-2]["id"]:
#    compressed_blocks[-2]["length"] += compressed_blocks.pop()["length"]
    
total_length = sum(block["length"] for block in decoded_blocks)

#hmm = 0
#for index, block in enumerate(decoded_blocks):
#    if block["id"] == "free":
#        hmm = index
#        break

#print(hmm)
#print(decoded_blocks[hmm])
#print(decoded_blocks[hmm-5:hmm+5])

#print(decoded_blocks)
checksum = 0
for index in range(total_length - 1, -1, -1):
    last_block = decoded_blocks[-1]
    while last_block["length"] <= 0:
        decoded_blocks.pop()
        last_block = decoded_blocks[-1]
    #if last_block["id"] == "free" and decoded_blocks[-2]["id"] == "free" and decoded_blocks[-3]["id"] == "free":
    #    print(len(decoded_blocks), last_block, decoded_blocks[-2], decoded_blocks[-3])
    if last_block["id"] != "free":
        checksum += last_block["id"] * index
    last_block["length"] -= 1

print(checksum)