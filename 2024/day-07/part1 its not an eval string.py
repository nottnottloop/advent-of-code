import itertools

with open('example.txt', 'r') as file:
    lines = [line.strip() for line in file]

test_equations = []
for line in lines:
    split = line.split(": ")
    value = int(split[0])
    numbers = [int(num) for num in split[1].split(" ")]
    test_equations.append({"value": value, "numbers": numbers})

print(test_equations)

equations_completed = []
for test_equation_index, test_equation in enumerate(test_equations):
    operator_position_count = len(test_equation["numbers"]) - 1
    test_cases = set(itertools.permutations('+*' * operator_position_count, operator_position_count))
    for test_case in test_cases:
        eval_string = str(test_equation["numbers"][0])
        for number in range(1, len(test_equation["numbers"])):
            eval_string += f" {test_case[number - 1]} {test_equation['numbers'][number]}"
        if eval(eval_string) == test_equation["value"]:
            equations_completed.append(test_equation_index)
            break

print(equations_completed)