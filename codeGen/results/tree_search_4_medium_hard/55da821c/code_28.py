import sys

n, m = map(int, input().split())
plants = []

for _ in range(n):
    s, x = map(float, input().split())
    plants.append((x, s))

# Sort plants by position
plants.sort()

# Group plants by species and calculate distances
species_plants = {}
total_replanting_cost = 0

prev_species = None
current_species_plants = []
for plant in plants:
    if plant[1] != prev_species:
        if prev_species is not None:
            total_replanting_cost += len(current_species_plants) - 1
        current_species_plants = [plant]
        prev_species = plant[1]
    else:
        current_species_plants.append(plant)

total_replanting_cost += len(current_species_plants) - 1

print(total_replanting_cost)
