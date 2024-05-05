import sys

n = int(sys.stdin.readline())
beacons = []

for _ in range(n):
    position, power = map(int, sys.stdin.readline().split())
    beacons.append((position, power))

beacons.sort()

destroyed_beacons = 0
last_position = float('inf')

for position, power in reversed(beacons):
    if last_position <= position - power:
        destroyed_beacons += 1
    last_position = position

new_beacon_position = int(sys.stdin.readline())
new_beacon_power = int(sys.stdin.readline())

destroyed_beacons += sum(1 for p, pw in beacons if new_beacon_position > p + pw)

print(destroyed_beacons)
