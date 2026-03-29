import sys

def max_power_range(b):
    return b

def solve(n, beacons):
    # Sort beacons by power level in descending order
    beacons.sort(key=lambda x: x[1], reverse=True)

    destroyed = 0
    for beacon in beacons:
        max_range = max_power_range(beacon[1])
        # Find all beacons to the left that fall within this power range
        for other_beacon in beacons[:beacons.index(beacon)]:
            if other_beacon[0] <= beacon[0] - max_range:
                destroyed += 1
                break

    return destroyed + 1  # Add the new beacon

n = int(sys.stdin.readline())
beacons = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    beacons.append((a, b))

print(solve(n, beacons))
