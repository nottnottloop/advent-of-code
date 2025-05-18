with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

raw_count = 0
parsed_count = 0
for line in lines:
    encoded_string = ""
    for i, c in enumerate(repr(line)):
        if c == '"':
            encoded_string += r"\""
        else:
            encoded_string += rf"{c}"
    print(encoded_string)
    raw_count += len(encoded_string)
    parsed_count += len(eval(encoded_string))

print("Raw count:", raw_count)
print("Parsed count:", parsed_count)
print(raw_count - parsed_count)