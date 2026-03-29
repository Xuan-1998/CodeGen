import sys

n = int(sys.stdin.readline())
beacons = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    beacons.append((a, b))

beacons.sort(key=lambda x: x[0])

min_power = float('inf')
max_power = 0
destroyed = 0

for a, b in beacons:
    min_power = min(min_power, b)
    max_power = max(max_power, b)
    destroyed += (b - min_power) // (max_power - min_power + 1)

print(destroyed)
