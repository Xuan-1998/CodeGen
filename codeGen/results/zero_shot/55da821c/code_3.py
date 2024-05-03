import sys
n, m = map(int, sys.stdin.readline().split())
species = [0] * (m + 1)
plants = []
for _ in range(n):
    s, x = map(float, sys.stdin.readline().split())
    plants.append((s, x))
plants.sort(key=lambda x: x[1])
print(min(1, n - m))  # Initial replanting
replanted = min(1, n - m)
for i in range(m):
    while plants and plants[0][0] == i + 1:
        _, _x = plants.pop(0)
        replanted += abs(_x) - len(plants)
print(replanted)
