import hashlib

with open('input.txt', 'r') as file:
    door_id = [line.strip() for line in file][0]

password = ""
i = 0
while len(password) < 8:
    hash = hashlib.md5(f"{door_id}{i}".encode()).hexdigest()
    if hash[0:5] == "00000":
        password += hash[5]
    i += 1

print(password)