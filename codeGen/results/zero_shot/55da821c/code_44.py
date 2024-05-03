import sys

n, m = map(int, sys.stdin.readline().split())
plants = []
for i in range(n):
    s, x = map(float, sys.stdin.readline().split())
    plants.append((s, x))

plants.sort(key=lambda x: x[1])

replantings = 0
for i, (s, x) in enumerate(plants):
    if s != i + 1:
        replantings += 1

print(replantings)
