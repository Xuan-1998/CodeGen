import sys

n = int(sys.stdin.readline())
beacons = []
for _ in range(n):
    pos, power = map(int, sys.stdin.readline().split())
    beacons.append((pos, power))

# Sort beacons by position
beacons.sort()

total_power = 0
max_power = 0

# Calculate total power at each position
for pos, power in beacons:
    if power > total_power:
        total_power = power
    max_power = max(max_power, total_power)

print(max_power)
