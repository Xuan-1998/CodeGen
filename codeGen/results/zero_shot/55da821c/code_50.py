import sys

n, m = map(int, input().split())
plants = []
for _ in range(n):
    s, x = map(float, input().split())
    plants.append((int(s), x))

plants.sort()

replanted = 0
sections = 1
prev_species = plants[0][0]
for plant in plants:
    if plant[0] != prev_species:
        sections += 1
    replanted += sections - 1

print(replanted)
