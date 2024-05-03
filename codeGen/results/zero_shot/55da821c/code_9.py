import sys

n, m = map(int, sys.stdin.readline().split())
plants = []

for _ in range(n):
    species, position = map(float, sys.stdin.readline().split())
    plants.append((species, position))

# Sort plants by position
plants.sort(key=lambda x: x[1])

# Group plants by species
species_plants = [[] for _ in range(m)]
for plant in plants:
    species_plants[plant[0] - 1].append(plant)

# Count the number of plants that need to be replanted
replanted_plants = 0
boundaries = [0] * (m - 1)
for i, species in enumerate(species_plants):
    for plant in species:
        if plant[1] > boundaries[i]:
            replanted_plants += 1

print(replanted_plants)
