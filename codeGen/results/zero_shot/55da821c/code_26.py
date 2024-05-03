import sys

n, m = map(int, input().split())
plants = []
for _ in range(n):
    s, x = map(float, input().split())
    plants.append((s, x))

plants.sort(key=lambda x: x[1])

min_replanted = 0
current_species = None
for i, (species, _) in enumerate(plants):
    if species != current_species:
        min_replanted += 1
        current_species = species

print(min_replanted)
