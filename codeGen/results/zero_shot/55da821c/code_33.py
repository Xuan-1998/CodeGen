import sys

n, m = map(int, input().split())
plants = []

for _ in range(n):
    s, x = map(float, input().split())
    plants.append((s, x))

plants.sort(key=lambda x: x[1])

species_count = {}

for s, _ in plants:
    if s not in species_count:
        species_count[s] = 0
    species_count[s] += 1

replantings = 0

for i, (s, _) in enumerate(species_count):
    if s != i + 1:  # mismatched species
        replantings += species_count[s] - 1  # need to replant all plants of this species

print(replantings)
