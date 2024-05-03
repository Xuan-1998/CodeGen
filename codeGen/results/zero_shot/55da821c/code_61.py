import sys

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
plants = []
for i in range(n):
    s, x = map(float, sys.stdin.readline().split())
    plants.append((s, x))

# Sort plants by species and position
plants.sort(key=lambda x: (x[0], x[1]))

# Initialize variables
replanted = 0
section_start = [0] * m

# Place each plant in its corresponding section
for s, x in plants:
    if section_start[s-1] == 0:
        # This is the first plant of this species; start a new section
        section_start[s-1] = x
    else:
        # This is not the first plant of this species; replant it
        replanted += 1

# Print the answer to stdout
print(replanted)
