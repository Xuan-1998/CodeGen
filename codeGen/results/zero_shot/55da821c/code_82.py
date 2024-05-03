import sys
from collections import defaultdict

n, m = map(int, input().split())
plants = []
species_positions = defaultdict(list)

for _ in range(n):
    species, position = map(float, input().split())
    plants.append((int(species), position))
    species_positions[int(species)].append(position)

plants.sort(key=lambda x: x[1])

replants_needed = 0
previous_species = None

for plant in plants:
    if plant[0] != previous_species:
        replants_needed += 1
    previous_species = plant[0]

print(replants_needed)
