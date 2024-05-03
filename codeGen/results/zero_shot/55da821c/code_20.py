import sys

n, m = map(int, sys.stdin.readline().split())
plants = []
for _ in range(n):
    s, x = map(float, sys.stdin.readline().split())
    plants.append((s, x))
plants.sort(key=lambda x: x[1])

counts = [0] * (m + 1)
borders = []

for s, x in plants:
    counts[s] += 1

min_replanting = sum(abs(counts[i] - (i + 1)) for i in range(m))
print(min_replanting)
