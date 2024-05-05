import sys

n = int(sys.stdin.readline())  # read number of beacons
beacon_positions_and_power_levels = []

for _ in range(n):
    position, power_level = map(int, sys.stdin.readline().split())
    beacon_positions_and_power_levels.append((position, power_level))

# TO DO: implement the logic for each case
