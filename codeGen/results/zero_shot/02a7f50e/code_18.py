import sys

n = int(sys.stdin.readline())
beacons = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    beacons.append((a, b))

beacons.sort()

destruction_count = 0
for i in range(n-1):
    for j in range(i+1):
        if beacons[i][0] - beacons[j][0] <= beacons[i][1]:
            destruction_count += 1
            break

new_beacon = map(int, sys.stdin.readline().split())
beacons.append(new_beacon)
destruction_count += 1

print(destruction_count)
