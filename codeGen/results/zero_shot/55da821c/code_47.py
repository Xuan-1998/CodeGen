n, m = map(int, input().split())
plants = []
for _ in range(n):
    species, x = map(float, input().split())
    plants.append((int(species), float(x)))

plants.sort(key=lambda x: x[1])

species_count = {}
for _, x in plants:
    species_index = int(x)
    if species_index not in species_count:
        species_count[species_index] = 0
    species_count[species_index] += 1

replantings = max(species_count.values()) - min(species_count.values())

print(replantings)
