import sys

n = int(sys.stdin.readline())
beacons = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    beacons.append((a, b))

beacons.sort(key=lambda x: x[0])

destroyed = 0
for i in range(n-1, -1, -1):
    position, power = beacons[i]
    destroyed_for_this_beacon = 0
    for j in range(i-1, -1, -1):
        other_position, _ = beacons[j]
        if abs(position - other_position) <= power:
            destroyed_for_this_beacon += 1
    destroyed += destroyed_for_this_beacon

new_position = int(sys.stdin.readline())
beacons.append((new_position, int(sys.stdin.readline())))

print(destroyed)
