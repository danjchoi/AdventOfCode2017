"""Generate all days for Advent of Code."""

for i in range(1, 26):
    s = 'day' + str(i) + '.py'
    with open(s, 'w') as file:
        file.write("\"\"\"Day " + str(i) + "\"\"\"\n")
