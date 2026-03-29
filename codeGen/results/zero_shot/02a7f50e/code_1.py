import sys

n = int(sys.stdin.readline())
beacons = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    beacons.append((y, x))  # store power level first for sorting purposes

beacons.sort()  # sort by power level (descending)

destroyed = 0
last_x = float('inf')  # initialize last_x to infinity

for y, x in beacons:
    if x <= last_x:  # new beacon doesn't destroy any existing ones
        last_x = x
    else:
        destroyed += 1

print(destroyed)
