# took 6 minutes to get the correct answer
import itertools
import copy
import json

# this json stuff is a result of me originally not collecting ids for successful equations correctly
with open('output.json', 'r') as file:
    jsonfile = json.load(file)

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

test_equations = []
for index, line in enumerate(lines):
    split = line.split(": ")
    value = int(split[0])
    numbers = [int(num) for num in split[1].split(" ")]
    test_equations.append({"value": value, "numbers": numbers, "id": index})

def generate_test_cases(test_equation):
    operator_position_count = len(test_equation["numbers"]) - 1
    return set(itertools.permutations('+*|' * operator_position_count, operator_position_count))

def calculate_accumulation_for_test_case(test_equation, test_case):
    accumulator = eval(f"{str(test_equation["numbers"][0])}")
    if len(test_case) == 0:
        return accumulator
    for operator_index in range(len(test_case)):
        if test_case[operator_index] != "|":
            eval_string = f"{str(test_case[operator_index])} {str(test_equation["numbers"][operator_index + 1])}"
            accumulator = eval(f"{accumulator} {eval_string}")
        else:
            accumulator = int(str(accumulator) + str(test_equation["numbers"][operator_index + 1]))
    return accumulator

mutated_test_equations = []
ultimate_mutated_test_equations = []
limit_to_numbers = 4
skip_everything = False
if not skip_everything:
    # Step 1: Reduce equations with more numbers than 6 into more equations
    for test_equation_index, test_equation in enumerate(test_equations):
        if len(test_equation["numbers"]) > limit_to_numbers:
            large_equation = copy.deepcopy(test_equation)
            remaining_numbers = large_equation["numbers"][limit_to_numbers:]
            shaved_off_numbers = large_equation["numbers"][:limit_to_numbers]
            frankenequation = {"numbers": shaved_off_numbers}
            test_cases = generate_test_cases(frankenequation)
            possible_outcomes = []
            for test_case in test_cases:
                possible_outcomes.append(calculate_accumulation_for_test_case(frankenequation, test_case))
            for possible_outcome in possible_outcomes:
                mutated_test_equations.append({"value": large_equation["value"], "numbers": [possible_outcome] + remaining_numbers, "id": test_equation["id"]})
        else:
            mutated_test_equations.append(copy.deepcopy(test_equation))

    # Step 2: https://i.kym-cdn.com/photos/images/newsfeed/001/554/866/4da.png
    for test_equation_index, test_equation in enumerate(mutated_test_equations):
        if len(test_equation["numbers"]) > limit_to_numbers:
            large_equation = copy.deepcopy(test_equation)
            remaining_numbers = large_equation["numbers"][limit_to_numbers:]
            shaved_off_numbers = large_equation["numbers"][:limit_to_numbers]
            frankenequation = {"numbers": shaved_off_numbers}
            test_cases = generate_test_cases(frankenequation)
            possible_outcomes = []
            for test_case in test_cases:
                possible_outcomes.append(calculate_accumulation_for_test_case(frankenequation, test_case))
            for possible_outcome in possible_outcomes:
                ultimate_mutated_test_equations.append({"value": large_equation["value"], "numbers": [possible_outcome] + remaining_numbers, "id": test_equation["id"]})
        else:
            ultimate_mutated_test_equations.append(copy.deepcopy(test_equation))

    # Step 3: Doing all of the smaller sized test equations after chunking them down
    equations_completed = set()
    for test_equation_index, test_equation in enumerate(ultimate_mutated_test_equations):
        print(f"{test_equation_index + 1} of {len(ultimate_mutated_test_equations)}")
        #print(f"id: {test_equation["id"]}")
        test_cases = generate_test_cases(test_equation)
        accumulator = 0
        for test_case in test_cases:
            if calculate_accumulation_for_test_case(test_equation, test_case) == test_equation["value"]:
                equations_completed.add(test_equation["id"])
                break
else:
    equations_completed = jsonfile

sum = 0
for successful_equation in equations_completed:
    sum += next(equation["value"] for equation in test_equations if equation["id"] == successful_equation)


#print(equations_completed)
print(sum)