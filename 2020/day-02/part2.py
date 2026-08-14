with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

passwords = []
    
for line in lines:
    split = line.split(" ")
    string = split[2]
    letter = split[1][0]
    pos1 = int(split[0].split("-")[0])
    pos2 = int(split[0].split("-")[1])
    passwords.append({"string": string, "letter": letter, "pos1": pos1, "pos2": pos2})

valid_passwords = 0

for password in passwords:
    letter_count = 0
    for i in [password["pos1"], password["pos2"]]:
        if password["string"][i - 1] == password["letter"]:
            letter_count += 1
    if letter_count == 1:
        valid_passwords += 1

print(valid_passwords)

