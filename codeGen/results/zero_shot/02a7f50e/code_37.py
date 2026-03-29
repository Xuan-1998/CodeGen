import sys

n = int(sys.stdin.readline())
positions = []
powers = []

for _ in range(n):
    pos, pow = map(int, sys.stdin.readline().split())
    positions.append(pos)
    powers.append(pow)

# Sort beacons by position and power level
positions.sort()
powers.sort()

min_destroyed = float('inf')

for i in range(len(powers) - 1):  # Try all possible new beacons
    pos, pow = positions[i], powers[i]
    destroyed = 0

    for j in range(i):
        if abs(positions[j] - pos) <= pow:
            destroyed += 1

    min_destroyed = min(min_destroyed, destroyed)

print(min_destroyed)
