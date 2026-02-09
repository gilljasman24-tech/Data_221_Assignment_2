import string

# Read all lines from the file
file = open("sample-file.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()

normalized_map = {}

# Normalize each line and store line numbers and original text
for index, line in enumerate(lines, start=1):
    original_line = line.rstrip("\n")
    normalized_line = original_line.lower()

    for char in string.whitespace + string.punctuation:
        normalized_line = normalized_line.replace(char, "")

    # Skip empty normalized lines
    if normalized_line == "":
        continue

    if normalized_line in normalized_map:
        normalized_map[normalized_line].append((index, original_line))
    else:
        normalized_map[normalized_line] = [(index, original_line)]

# Collect only near-duplicate sets
duplicate_sets = []

for key in normalized_map:
    if len(normalized_map[key]) > 1:
        duplicate_sets.append(normalized_map[key])

# Print the number of near-duplicate sets
print("Number of near-duplicate sets:", len(duplicate_sets))
print()

# Print the first two sets found
for i in range(min(2, len(duplicate_sets))):
    print("Set", i + 1)
    for line_number, text in duplicate_sets[i]:
        print(str(line_number) + ":", text)
    print()