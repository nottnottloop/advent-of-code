import hashlib

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

num = 0
while True:
    num += 1
    s = f"{lines[0]}{str(num)}"
    hash = hashlib.md5(s.encode())
    hex = hash.hexdigest()
    if hex.startswith("000000"):
        print(hex)
        print(num)
        break