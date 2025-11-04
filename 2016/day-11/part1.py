import collections
import itertools
# for the first time i'm completely manually parsing the example and input to make it more machine readable
# eg the example becomes
# myexample:
#HM LM
#HG
#LG
#nothing

with open('example1.txt', 'r') as file:
    lines = [line.strip() for line in file]

initial_state = {}

for index, line in enumerate(lines):
    if line != "nothing":
        initial_state[index+1] = frozenset(line.split())
    else:
        initial_state[index+1] = frozenset()

initial_state["e"] = 1
initial_state["s"] = 0

states = collections.deque([frozenset(initial_state.items())])
visited = set(frozenset(initial_state.items()))

while states:
    current_state = dict(states.popleft())

    possible_next_floors = []
    for vector in [-1, 1]:
        if current_state["e"] + vector in [1, 2, 3, 4]:
            possible_next_floors.append(current_state["e"] + vector)
    
    current_floor = set(current_state[current_state["e"]])
    possible_items_to_take = list()
    for i in range(1, 3):
        possible_items_to_take.extend(list(itertools.combinations(current_floor, i)))

    next_possible_states = []
    for next_floor in possible_next_floors:
        new_floor = set(current_state[next_floor])
        for items in possible_items_to_take:
            combined_items = set(items) | new_floor
            print(combined_items)
    #print(possible_items_to_take)

    #for next_state in next_possible_states:
    #    if next_state not in visited:
    #        visited.add(next_state)
    #        states.append(next_state)

#print(visited)