import sys

# Read input
n = int(sys.stdin.readline())
positions = []
powers = []

for _ in range(n):
    pos, power = map(int, sys.stdin.readline().split())
    positions.append(pos)
    powers.append(power)

# Sort the beacons by their positions
sorted_positions = sorted(zip(positions, powers))

# Initialize variables to keep track of the number of active beacons and the maximum position reached so far
active_beacons = n
max_position_reached = max(sorted_positions)[0]

# Iterate over the beacons in reverse order (from right to left)
for pos, power in reversed(sorted_positions):
    # If the current beacon's position is less than or equal to the maximum position reached so far,
    # it means that this beacon will not destroy any other beacons
    if pos <= max_position_reached:
        active_beacons -= 1
    else:
        # Otherwise, subtract the number of beacons within its power range from the total number of active beacons
        active_beacons -= (max_position_reached - pos + power) // power

print(active_beacons)
