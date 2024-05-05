import sys

n = int(sys.stdin.readline())
beacons = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    beacons.append((a, b))

beacons.sort()

min_destroyed = 0
prev_pos = -1

for a, b in beacons:
    power_range = a + b
    if prev_pos >= power_range:
        min_destroyed += 1
    prev_pos = a

print(min_destroyed)
