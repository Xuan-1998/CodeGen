import sys

# Read input
n = int(sys.stdin.readline())
beacons = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    beacons.append((a, b))

# Sort beacons by position
beacons.sort()

# Initialize minimum number of destroyed beacons
min_destroyed = 0

# Iterate through sorted beacons and add new one
for i in range(n):
    # Add new beacon to the right of all existing beacons
    new_beacon_pos, _ = beacons[i]
    min_destroyed += sum(b[1] > b[0] for b in beacons[:i])  # Calculate destroyed beacons

print(min_destroyed)
