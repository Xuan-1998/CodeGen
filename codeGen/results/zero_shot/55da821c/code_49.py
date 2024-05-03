import sys

plants_by_species = {}

for _ in range(int(sys.stdin.readline())):
    species, x = map(int, sys.stdin.readline().split())
    if species not in plants_by_species:
        plants_by_species[species] = []
    plants_by_species[species].append(x)

for species in plants_by_species.values():
    species.sort()

sections = [[] for _ in range(m)]
for species, x_coords in plants_by_species.items():
    for x in x_coords:
        section_idx = species - 1
        sections[section_idx].append(x)

replantings = sum(len(section) - 1 for section in sections)
print(replantings)
