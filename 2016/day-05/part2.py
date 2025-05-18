import hashlib

with open('input.txt', 'r') as file:
    door_id = [line.strip() for line in file][0]

password = ["H" for i in range(8)]
assigned = []
i = 0
while "H" in password:
    hash = hashlib.md5(f"{door_id}{i}".encode()).hexdigest()
    if hash[0:5] == "00000":
        if hash[5] not in assigned and hash[5] in map(str, [0,1,2,3,4,5,6,7]):
            password[int(hash[5])] = hash[6]
            assigned.append(hash[5])
    i += 1

print("".join(password))