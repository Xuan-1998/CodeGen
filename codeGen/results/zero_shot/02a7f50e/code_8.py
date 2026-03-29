import sys

n = int(sys.stdin.readline())
beacon_positions = []
beacon_powers = []

for _ in range(n):
    position, power = map(int, sys.stdin.readline().split())
    beacon_positions.append(position)
    beacon_powers.append(power)

beacon_positions, beacon_powers = zip(*sorted(zip(beacon_positions, beacon_powers)))

total_destroyed = 0

for i in range(n):
    power_range = beacon_powers[i]
    
    beacons_in_power_range = 0
    
    for j in range(i, -1, -1):
        if beacon_positions[j] <= beacon_positions[i] + power_range:
            beacons_in_power_range += 1
        else:
            break
    
    total_destroyed += beacons_in_power_range - 1

print(total_destroyed)
