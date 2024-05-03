import sys

n, m = map(int, input().split())
plants = []

for _ in range(n):
    s_i, x_i = map(float, input().split())
    plants.append((s_i, x_i))

plants.sort(key=lambda x: x[1])

sections = {}
replanted = 0

for plant in plants:
    species, pos = plant
    if species not in sections:
        sections[species] = []
    sections[species].append(pos)

for section in range(1, m+1):
    for pos in sections.get(section, []):
        replanted += 1

print(replanted)
