import sys

n, m = map(int, sys.stdin.readline().split())
plants = []
for _ in range(n):
    s, x = map(float, sys.stdin.readline().split())
    plants.append((s, x))

plants.sort(key=lambda x: x[1])

replanted = 0
species_count = [0] * m

for s, x in plants:
    species_count[s-1] += 1
    if s != species_count.index(max(species_count)):
        replanted += 1

print(replanted)
