with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

raw_rules = lines[0:lines.index("")]
raw_updates = lines[lines.index("")+1:]
rules = []
updates = []
for rule in raw_rules:
    before, after = rule.split('|')
    rules.append({"before": before, "after": after})
for update in raw_updates:
    to_append = update.split(',')
    updates.append(to_append)
    
def check_update(update):
    good_update = True
    index_to_move = None
    direction = None
    for index, num in enumerate(update):
        for look_behind in update[0:index]:
            result = list(filter(lambda rule: rule["before"] == num and rule["after"] == look_behind, rules))
            if result:
                good_update = False
        for look_ahead in update[index+1:]:
            result = list(filter(lambda rule: rule["after"] == num and rule["before"] == look_ahead, rules))
            if result:
                good_update = False
    return good_update

bad_updates = []
for update_index, update in enumerate(updates):
    result = check_update(update)
    if not result:
        bad_updates.append(update)

def bubble_sort(update):
    for i in range(len(update) - 1):
        swapped = False
        for index in range(len(update) - i - 1):
            filter_obj = list(filter(lambda rule: rule["after"] == update[index] and rule["before"] == update[index+1], rules))
            if filter_obj:
                update[index], update[index+1] = update[index+1], update[index]
                swapped = True

        if not swapped:
            break
    return update

for index, bad_update in enumerate(bad_updates):
    bad_updates[index] = bubble_sort(bad_update)
    

sum = 0
for update in bad_updates:
    sum += int(update[(len(update) // 2)])

#print(rules)
#print(bad_updates)
print(sum)