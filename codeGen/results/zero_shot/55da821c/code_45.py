import sys

n, m = map(int, sys.stdin.readline().split())
plants = []

for i in range(n):
    s, x = map(float, sys.stdin.readline().split())
    plants.append((s, x))

plants.sort(key=lambda x: x[1])

replanted = 0
species_count = [0] * m

for p in plants:
    species_count[p[0] - 1] += 1

for i in range(1, m):
    replanted += max(species_count[i-1], species_count[i])

print(replanted)
