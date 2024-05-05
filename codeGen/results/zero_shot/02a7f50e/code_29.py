import sys

n = int(sys.stdin.readline())
beacons = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    beacons.append((a, b))
beacons.sort(key=lambda x: x[0])

destroyed = 0
for i in range(n):
    if i == 0 or beacons[i-1][1] >= beacons[i][1]:
        destroyed += 1

print(destroyed)
