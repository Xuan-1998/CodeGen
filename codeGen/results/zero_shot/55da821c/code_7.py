import sys

n, m = map(int, sys.stdin.readline().split())
plants = []

for _ in range(n):
    s, x = map(float, sys.stdin.readline().split())
    plants.append((s, x))

plants.sort(key=lambda x: x[1])

sections = [[] for _ in range(m)]

for s, x in plants:
    sections[s-1].append((s, x))

replanted = 0

for i, section in enumerate(sections):
    if len(section) > 1:
        replanted += len(section) - 1
    elif section[0][0] != i+1:
        replanted += len(section)

print(replanted)
