import sys

n = int(sys.stdin.readline())
beacons = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    beacons.append((a, b))

# Sort beacons by position
beacons.sort()

destroyed = 0

for i in range(1, len(beacons)):
    if beacons[i][0] - beacons[0][0] > beacons[i-1][1]:
        destroyed += 1

print(destroyed)
