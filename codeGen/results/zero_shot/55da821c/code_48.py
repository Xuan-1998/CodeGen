import sys

n, m = map(int, input().split())
plants = [list(map(int, input().split())) for _ in range(n)]

sections = [[] for _ in range(m)]
for plant in plants:
    species, x = plant
    sections[species - 1].append((x, species))

replantings = 0
for section in sections:
    if len(section) > 1:
        replantings += len(section) - 1

print(replantings)
