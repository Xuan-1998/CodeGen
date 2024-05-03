import sys

n, m = map(int, sys.stdin.readline().split())
plants = []
for i in range(n):
    s, x = map(float, sys.stdin.readline().split())
    plants.append((s, x))

plants.sort(key=lambda x: x[1])

arrangement = [[] for _ in range(m)]
replanted = 0

for s, x in plants:
    for i in range(m):
        if arrangement[i] == [] or arrangement[i][0] == s:
            arrangement[i].append(s)
            break
    else:  # plant is not in its correct section, increment replanted count
        replanted += 1

print(replanted)
