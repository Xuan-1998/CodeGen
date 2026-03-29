import sys

n = int(sys.stdin.readline())
beacons = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    beacons.append((a, b))

beacons.sort(key=lambda x: x[0], reverse=True)

destroyed = 0
last_right = -1

for a, b in beacons:
    if a > last_right + 1:
        destroyed += 1
        last_right = a - 1

print(destroyed)
