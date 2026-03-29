import sys

n = int(sys.stdin.readline())
beacons = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    beacons.append((x, y))

# Sort the beacons by their power levels
beacons.sort(key=lambda x: x[1], reverse=True)

# Initialize the minimum number of destroyed beacons to 0
min_destroyed = 0

# Iterate over the sorted beacons
for beacon in beacons:
    # For each beacon, find the maximum position that would not destroy it
    max_pos = 0
    for existing_beacon in beacons:
        if existing_beacon[0] <= max_pos + (beacon[1] - beacon[0]):
            max_pos = existing_beacon[0]
            break
    # Update the minimum number of destroyed beacons
    min_destroyed += len(beacons) - (max_pos + 1)

print(min_destroyed)
