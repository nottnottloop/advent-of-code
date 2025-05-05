with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

alphabet = "abcdefghijklmnopqrstuvwxyz"
priorities = {letter:value+1 for value,letter in enumerate(alphabet+alphabet.upper())}

shared_characters = []
for line in lines:
    shared_characters.append(list(set(line[:len(line)//2]) & set(line[len(line)//2:]))[0]) 
    
print(sum(priorities[c] for c in shared_characters))