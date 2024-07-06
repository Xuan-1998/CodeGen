import sys

n = int(sys.stdin.readline())
beacons = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    beacons.append((a, b))
beacons.sort()

destroyed = 0
max_power = 0
for a, b in beacons:
    if b > max_power:
        destroyed += 1
        max_power = b

new_a, new_b = map(int, sys.stdin.readline().split())
beacons.append((new_a, new_b))
max_power = 0
for a, b in beacons:
    if b > max_power:
        destroyed += 1
        max_power = b

print(destroyed)
