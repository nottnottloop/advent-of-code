with open(f'input.txt', 'r') as file:
    lines = [line.strip() for line in file][2:]

filepath = ["/"]
filesystem = {"/": {}}
for line in lines:
    args = line.split(" ")
    # Command
    if args[0] == "$":
        if args[1] == "cd":
            if args[2] != "..":
                filepath.append(args[2] + "/")
            else:
                # this was cool
                #filepath = "/".join(filepath.split("/")[:-2]) + "/"
                filepath.pop()
    # Directories and files
    if args[0] != "$":
        if args[0] == "dir":
            filesystem["".join(filepath) + args[1] + "/"] = {}
        else:
            filesystem["".join(filepath)][args[1]] = int(args[0])

total_size = 0
answer = 0
checked_dirs = []
def get_total_dir_size(dir):
    global total_size, checked_dirs
    total_size += sum(filesystem[dir].values())
    checked_dirs.append(dir)
    if total_size < 100000:
        for key in filesystem.keys():
            if key.startswith(dir) and key != dir and key not in checked_dirs:
                get_total_dir_size(key)
    

for dir in filesystem.keys():
    total_size = 0
    checked_dirs = []
    get_total_dir_size(dir)
    if total_size < 100000:
        answer += total_size

for f in filesystem:
    print(f)
print(answer)