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
    
good_updates = []
for update_index, update in enumerate(updates):
    good_update = True
    for index, num in enumerate(update):
        for look_behind in update[0:index]:
            if list(filter(lambda rule: rule["before"] == num and rule["after"] == look_behind, rules)):
                good_update = False
        for look_ahead in update[index+1:]:
            if list(filter(lambda rule: rule["after"] == num and rule["before"] == look_ahead, rules)):
                good_update = False
    if good_update:
        good_updates.append(update)

print("Good updates:")
print(good_updates)

sum = 0
for good_update in good_updates:
    sum += int(good_update[(len(good_update) // 2)])

print(sum)