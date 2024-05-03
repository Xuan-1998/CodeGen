import sys

n, m = map(int, sys.stdin.readline().split())
plants = []
for i in range(n):
    s, x = map(float, sys.stdin.readline().split())
    plants.append((s, x))

plants.sort(key=lambda x: x[1])

species_groups = {}
for s, x in plants:
    if s not in species_groups:
        species_groups[s] = []
    species_groups[s].append((s, x))

replants = 0
for s, group in species_groups.items():
    max_x = max(x for _, x in group)
    replants += len(group) - (max_x + 1) // m

print(replants)
