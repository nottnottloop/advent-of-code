with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]
    
gate_map = {
    "AND": "&",
    "LSHIFT": "<<",
    "NOT": "~",
    "OR": "|",
    "RSHIFT": ">>",
}

signals = {}
counter = 0
while lines:
    if counter > len(lines) - 1:
        counter = 0
    statement, wire = lines[counter].split(" -> ")
    no_gate = True
    for gate in gate_map.keys():
        if gate in statement:
            no_gate = False
            if gate == "NOT":
                operands = [statement.split(f"{gate} ")[1]]
            else:
                operands = statement.split(f" {gate} ")
            #print(operands)
            if all(key in signals for key in list(filter(lambda o: not o.isdigit(), operands))):
                one = int(operands[0]) if operands[0].isdigit() else "signals[operands[0]]"
                if gate == "NOT":
                    signals[wire] = eval(f"{gate_map[gate]} {one}") & 0xFFFF
                else:
                    one = int(operands[0]) if operands[0].isdigit() else "signals[operands[0]]"
                    two = int(operands[1]) if operands[1].isdigit() else "signals[operands[1]]"
                    signals[wire] = eval(f"{one} {gate_map[gate]} {two}") & 0xFFFF
                lines.pop(counter)
    if no_gate:
        try:
            signals[wire] = int(statement) & 0xFFFF
            lines.pop(counter)
        except:
            if statement in signals:
                signals[wire] = signals[statement] & 0xFFFF
                lines.pop(counter)
    counter += 1

print(signals)