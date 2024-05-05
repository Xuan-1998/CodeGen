n = int(input())
beacons = []
for _ in range(n):
    a, b = map(int, input().split())
    beacons.append((a, b))

beacons = sorted(beacons, key=lambda x: x[0], reverse=True)

destroyed = 0
for i, (a, b) in enumerate(beacons):
    destroyed_count = 0
    for j in range(i+1):
        if beacons[j][1] >= b:
            destroyed_count += 1
    destroyed += destroyed_count

new_beacon_position = max([x[0] for x in beacons]) + 1
new_beacon_power = min(beacons, key=lambda x: x[1])[1]
beacons.append((new_beacon_position, new_beacon_power))

print(destroyed)
