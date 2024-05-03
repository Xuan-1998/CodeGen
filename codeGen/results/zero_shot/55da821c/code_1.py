import sys

n, m = map(int, sys.stdin.readline().split())
plants = []

for i in range(n):
    s_i, x_i = map(float, sys.stdin.readline().split())
    plants.append((x_i, s_i))

plants.sort()

species_count = {}

for plant in plants:
    x, s = plant
    if s not in species_count:
        species_count[s] = 0
    species_count[s] += 1

replantings = 0

for i in range(1, m):
    if species_count[i] > 0:
        replantings += species_count[i]

print(replantings)
