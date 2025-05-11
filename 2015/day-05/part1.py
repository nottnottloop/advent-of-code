with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

nice_string_count = 0
bad_strings = ["ab", "cd", "pq", "xy"]
for line in lines:
    vowel_count = 0
    twice_in_a_row = False
    last_character = "%"
    contains_bad_string = False
    for c in line:
        if c in list("aeiou"):
            vowel_count += 1
        if f"{last_character}{c}" in bad_strings:
            contains_bad_string = True
            break
        if last_character == c:
            twice_in_a_row = True
        last_character = c
    if vowel_count >= 3 and twice_in_a_row and not contains_bad_string:
        nice_string_count += 1

print(nice_string_count)