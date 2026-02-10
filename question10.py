def find_lines_containing(filename, keyword):
    """
    Returns a list of (line_number, line_text) for lines that contain
    the given keyword (case-insensitive). Line numbers start at 1.
    """
    matches = []

    file = open(filename, "r", encoding="utf-8")
    lines = file.readlines()
    file.close()

    for index, line in enumerate(lines):
        if keyword.lower() in line.lower():
            matches.append((index + 1, line.strip()))

    return matches


# Test the function
results = find_lines_containing("sample-file.txt", "lorem")

print("Number of matching lines:", len(results))
print()

for line_number, text in results[:3]:
    print(f"{line_number}: {text}")
