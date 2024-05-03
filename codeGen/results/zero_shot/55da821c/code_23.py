import sys

n, m = map(int, input().split())
plants = []

for _ in range(n):
    s, x = map(float, input().split())
    plants.append((s, x))

# Sort plants by position
plants.sort(key=lambda x: x[1])

# Group plants by species
species_plants = {}
for plant in plants:
    if plant[0] not in species_plants:
        species_plants[plant[0]] = []
    species_plants[plant[0]].append(plant)

# Find optimal position for each species
min_replanted = 0
for species, plants_of_species in species_plants.items():
    left, right = 0, max(plant[1] for plant in plants_of_species)
    while left < right:
        mid = (left + right) / 2
        if all(plant[1] <= mid for plant in plants_of_species):
            right = mid
        else:
            left = mid
    min_replanted += len(plants_of_species) - 1

print(min_replanted)
