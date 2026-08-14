with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

passwords = []
    
for line in lines:
    split = line.split(" ")
    string = split[2]
    letter = split[1][0]
    min = int(split[0].split("-")[0])
    max = int(split[0].split("-")[1])
    passwords.append({"string": string, "letter": letter, "min": min, "max": max})

valid_passwords = 0

for password in passwords:
    letter_count = 0
    for letter in password["string"]:
        if letter == password["letter"]:
            letter_count += 1
    if letter_count >= password["min"] and letter_count <= password["max"]:
        valid_passwords += 1

print(valid_passwords)

