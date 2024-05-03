import sys

n, m = map(int, sys.stdin.readline().split())
plants = []

for i in range(n):
    s, x = map(float, sys.stdin.readline().split())
    plants.append((s, x))

# Sort plants by position
plants.sort(key=lambda x: x[1])

# Place borders to divide the greenhouse into m sections
borders = [0]
for i in range(1, m):
    # Find the first plant of species i+1 and place a border before it
    for j in range(borders[-1], len(plants)):
        if plants[j][0] == i + 1:
            borders.append(plants[j][1])
            break

# Count the minimum replanting needed
replanted = 0
for i in range(1, m):
    # Replant all plants of species i+1 to section i
    for j in range(borders[i-1], len(plants)):
        if plants[j][0] == i + 1:
            replanted += 1

print(replanted)
