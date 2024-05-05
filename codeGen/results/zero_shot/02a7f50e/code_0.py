destroyed = 0
max_power = 0

for a, b in beacons:
    # simulate activation of current beacon
    destroyed_at_most = 0
    for i in range(len(beacons) - 1):
        if beacons[i][0] < a and beacons[i][1] <= b:  # within power range
            destroyed_at_most += 1
    destroyed += destroyed_at_most

print(destroyed)
