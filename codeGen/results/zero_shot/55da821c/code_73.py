import sys

n, m = map(int, sys.stdin.readline().split())
plants = []

for i in range(n):
    s, x = map(float, sys.stdin.readline().split())
    plants.append((s, x))

plants.sort(key=lambda x: x[1])

species_counts = {}

for s, _ in plants:
    if s not in species_counts:
        species_counts[s] = 0
    species_counts[s] += 1

replantings = 0

for i in range(1, m):
    replantings += max(species_counts.get(i, 0) - species_counts.get(i-1, 0), 0)

print(replantings)
