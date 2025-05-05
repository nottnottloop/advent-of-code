from collections import namedtuple

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

Round = namedtuple("Round", ("opponent", "me"))
rounds = []
for line in lines:
    rounds.append(Round(line.split(" ")[0], line.split(" ")[1]))    
    
score = 0
weapon_score = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}
for round in rounds:
    if (round.opponent == "A" and round.me == "Y") or (round.opponent == "B" and round.me == "Z") or (round.opponent == "C" and round.me == "X"):
        score += 6
    elif (round.opponent == "A" and round.me == "X") or (round.opponent == "B" and round.me == "Y") or (round.opponent == "C" and round.me == "Z"):
        score += 3
    score += weapon_score[round.me]
    
print(score)