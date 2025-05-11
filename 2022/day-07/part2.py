with open(f'input.txt', 'r') as file:
    lines = [line.strip() for line in file][2:]

unused_space = 70000000
unused_space_needed = 30000000
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
checked_dirs = []
directories_by_space = []
def get_total_dir_size(dir):
    global total_size, checked_dirs
    total_size += sum(filesystem[dir].values())
    checked_dirs.append(dir)
    for key in filesystem.keys():
        if key.startswith(dir) and key != dir and key not in checked_dirs:
            get_total_dir_size(key)
    

for dir in filesystem.keys():
    total_size = 0
    checked_dirs = []
    get_total_dir_size(dir)
    if dir == "/":
        unused_space -= total_size
    directories_by_space.append(total_size)

for f in filesystem:
    print(f)

directories_by_space.sort()
for directory_size in directories_by_space:
    if unused_space + directory_size > unused_space_needed:
        print(f"Size to delete: {directory_size}")
        break
#print(directories_by_space)