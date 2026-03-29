import sys

n = int(sys.stdin.readline())
beacons = []
for i in range(n):
    pos, power = map(int, sys.stdin.readline().split())
    beacons.append((pos, power))

# Sort the beacons by their positions
beacons.sort()

total_destroyed = 0
for i in range(1, n):
    if beacons[i][0] > beacons[i-1][0]:
        total_destroyed += 1

print(total_destroyed)
