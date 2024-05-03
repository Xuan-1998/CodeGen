import sys

n, m = map(int, sys.stdin.readline().split())
plants = []

for _ in range(n):
    s, x = map(float, sys.stdin.readline().split())
    plants.append((s, x))

plants.sort(key=lambda x: x[1])

min_replanted = 0
prev_species = None

for plant in plants:
    if plant[0] != prev_species:
        min_replanted += 1
    prev_species = plant[0]

print(min_replanted)
