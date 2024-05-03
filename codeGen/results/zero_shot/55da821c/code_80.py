import sys

# Read input
n, m = map(int, sys.stdin.readline().split())
plants = []
for _ in range(n):
    species, x = map(float, sys.stdin.readline().split())
    plants.append((int(species), x))

# Sort plants by x-coordinate
plants.sort(key=lambda x: x[1])

# Initialize the sections
sections = [[] for _ in range(m)]

# Group plants by species and count replantings
replanted = 0
for plant in plants:
    species, x = plant
    section = species - 1  # Species-based indexing (0-indexed)
    if not sections[section]:
        sections[section].append(plant)
    else:
        replanted += 1

# Print the result
print(replanted)
