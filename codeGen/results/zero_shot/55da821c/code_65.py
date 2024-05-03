import sys

n, m = map(int, sys.stdin.readline().split())
plants = []

for i in range(n):
    s_i, x_i = map(float, sys.stdin.readline().split())
    plants.append((s_i, x_i))

plants.sort(key=lambda x: x[1])

species_plants = {}
for plant in plants:
    s_i, x_i = plant
    if s_i not in species_plants:
        species_plants[s_i] = []
    species_plants[s_i].append(x_i)

replantings = 0
for species in species_plants.values():
    max_diff = 0
    prev_x = None
    for x_i in species:
        if prev_x is not None:
            diff = x_i - prev_x
            max_diff = max(max_diff, diff)
        prev_x = x_i
    replantings += max_diff // (m - 1) + 1

print(replantings)
