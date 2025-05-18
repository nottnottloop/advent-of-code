with open('example.txt', 'r') as file:
    lines = [line.strip() for line in file]

raw_count = 0
parsed_count = 0
for line in lines:
    parsed_count += len(eval(line))
    print(repr(line))
    print(line.encode("raw_unicode_escape"))
    #raw_count += len(encoded_string)

print("Raw count:", raw_count)
print("Parsed count:", parsed_count)
print(raw_count - parsed_count)