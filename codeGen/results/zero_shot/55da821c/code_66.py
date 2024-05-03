import sys

# Read input integers n and m
n, m = map(int, sys.stdin.readline().split())

# Read n lines, each containing an integer s_i and a real number x_i
plants = []
for _ in range(n):
    s_i, x_i = map(float, sys.stdin.readline().split())
    plants.append((s_i, x_i))

# Sort the plants by their positions
plants.sort(key=lambda x: x[1])

# Group the plants by species
species_plants = {}
for plant in plants:
    if plant[0] not in species_plants:
        species_plants[plant[0]] = []
    species_plants[plant[0]].append(plant)

# Calculate the minimum number of replanting steps
replant_steps = 0
for species in species_plants.values():
    section_length = (species[-1][1] - species[0][1]) / len(species)
    replant_steps += int(section_length) - 1

print(replant_steps)
