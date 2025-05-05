with open('example.txt', 'r') as file:
    lines = [line.strip() for line in file]
    lines = [line for line in lines if line != ""]

claw_machines = []
# quick and dirty input parsing
for index, line in enumerate(lines):
    if "Button A" in line:
        claw_machine = {"a": {}, "b": {}, "prize": {}}
        sub = line.split("Button A: ")[1]
        sub = sub.split(", ")
        x_val = sub[0].split("X+")[1]
        y_val = sub[1].split("Y+")[1]
        claw_machine["a"]["x"] = int(x_val)
        claw_machine["a"]["y"] = int(y_val)
    elif "Button B" in line:
        sub = line.split("Button B: ")[1]
        sub = sub.split(", ")
        x_val = sub[0].split("X+")[1]
        y_val = sub[1].split("Y+")[1]
        claw_machine["b"]["x"] = int(x_val)
        claw_machine["b"]["y"] = int(y_val)
    elif "Prize" in line:
        sub = line.split("Prize: ")[1]
        sub = sub.split(", ")
        x_val = sub[0].split("X=")[1]
        y_val = sub[1].split("Y=")[1]
        claw_machine["prize"] = (int(x_val), int(y_val))
        claw_machines.append(claw_machine)

lowest_tokens = {}
# yeah we're brute forcing this to get fucked in part 2
for claw_machine_index, claw_machine in enumerate(claw_machines):
    lowest_tokens[claw_machine_index] = 99999999999999999999999999999
    prize_won_once = False
    for a_pushes in range(1, 101):        
        for b_pushes in range(1, 101):
            x = (claw_machine["a"]["x"] * a_pushes) + (claw_machine["b"]["x"] * b_pushes)
            y = (claw_machine["a"]["y"] * a_pushes) + (claw_machine["b"]["y"] * b_pushes)
            tokens_spent = a_pushes * 3 + b_pushes
            if (x, y) == claw_machine["prize"]:
                prize_won_once = True
                if tokens_spent < lowest_tokens[claw_machine_index]:
                    lowest_tokens[claw_machine_index] = tokens_spent
    if not prize_won_once:
        lowest_tokens[claw_machine_index] = 0

#print(claw_machines)
print(lowest_tokens)
print(sum(v for v in lowest_tokens.values()))