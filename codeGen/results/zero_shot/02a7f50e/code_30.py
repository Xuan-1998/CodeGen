import sys

n = int(sys.stdin.readline())
beacons = []

# Read in the beacons and sort them by position (descending)
for i in range(n):
    a_i, b_i = map(int, sys.stdin.readline().split())
    beacons.append((a_i, b_i))
beacons.sort(key=lambda x: x[0], reverse=True)

destroyed = 0

for i in range(n):
    a_i, b_i = beacons[i]
    # Check if adding this beacon would destroy any existing ones
    destroyed += len([x for x in beacons[:i] if abs(a_i - x[0]) <= b_i])

print(destroyed)
