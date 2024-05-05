n = int(input())
beacons = []
for _ in range(n):
    a, b = map(int, input().split())
    beacons.append((a, b))

beacons.sort(reverse=True)

destroyed = 0
max_power = max(b for _, b in beacons)

for a, b in beacons:
    range_ = max_power - b
    for i in range(len(beacons) - 1, -1, -1):
        if beacons[i][0] < a and beacons[i][1] > range_:
            destroyed += 1
            del beacons[i]
            break

print(destroyed)
