import sys

n, m = map(int, input().split())
plants = []

for _ in range(n):
    species, position = map(float, input().split())
    plants.append((int(species), float(position)))

plants.sort(key=lambda x: x[1])

borders = [0]
section = 1
replanted = 0

for plant in plants:
    if plant[0] != section:
        borders.append(plant[1])
        section += 1
    replanted += len(borders) - 1

print(replanted)
