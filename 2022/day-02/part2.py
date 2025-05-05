from collections import namedtuple

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

Round = namedtuple("Round", ("opponent", "outcome"))
rounds = []
# no bro, we're not doing this
weapon_map = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}
outcome_map = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}
for line in lines:
    str = line.split(" ")
    rounds.append(Round(weapon_map[str[0]], outcome_map[str[1]]))    

points_map = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}
map_map = {
    "draw": {"rock":"rock", "paper":"paper", "scissors":"scissors"},
    "win": {"rock":"paper", "paper":"scissors", "scissors":"rock"},
    "lose": {"rock":"scissors", "paper":"rock", "scissors":"paper"},
}

score = 0
for round in rounds:
    weapon = map_map[round.outcome][round.opponent]
    score += points_map[weapon]
    if round.outcome == "draw":
        score += 3
    elif round.outcome == "win":
        score += 6
    
print(score)