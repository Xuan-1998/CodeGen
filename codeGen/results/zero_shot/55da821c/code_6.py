import sys

n, m = map(int, sys.stdin.readline().split())
species_plants = {}

for _ in range(n):
    species, position = map(float, sys.stdin.readline().split())
    if species not in species_plants:
        species_plants[species] = []
    species_plants[species].append(position)

replanted_count = 0
sections = [i for i in range(1, m+1)]

for species, positions in species_plants.items():
    section_index = sections.index(species)
    replanted_count += len(positions) - (section_index + 1)

print(replanted_count)
