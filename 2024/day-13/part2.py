from sympy import symbols, Eq, solve

with open('input.txt', 'r') as file:
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
        extra_sauce = 10000000000000
        sub = line.split("Prize: ")[1]
        sub = sub.split(", ")
        x_val = int(sub[0].split("X=")[1]) + extra_sauce
        y_val = int(sub[1].split("Y=")[1]) + extra_sauce
        claw_machine["prize"] = (x_val, y_val)
        claw_machines.append(claw_machine)

lowest_tokens = 0
# part 2 called and it's not happy
for claw_machine_index, claw_machine in enumerate(claw_machines):
    a, b = symbols("a, b", integer=True)
    
    eq1 = Eq(claw_machine["a"]["x"] * a + claw_machine["b"]["x"] * b, claw_machine["prize"][0])
    eq2 = Eq(claw_machine["a"]["y"] * a + claw_machine["b"]["y"] * b, claw_machine["prize"][1])
    
    solution = solve((eq1, eq2))
    if solution:
        lowest_tokens += solution[a] * 3 + solution[b]

#print(claw_machines)
print(lowest_tokens)
#print(sum(v for v in lowest_tokens.values()))