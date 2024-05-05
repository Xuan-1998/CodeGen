import sys

n = int(sys.stdin.readline())
beacons = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    beacons.append((a, b))
beacons.sort(key=lambda x: x[0])

destroyed = 0
for i in range(n-1, -1, -1):
    pos, power = beacons[i]
    for j in range(i-1, -1, -1):
        prev_pos, _ = beacons[j]
        if prev_pos < pos and power > 0:
            destroyed += 1
            break

print(destroyed)
