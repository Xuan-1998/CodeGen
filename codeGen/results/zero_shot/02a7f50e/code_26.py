import sys

n = int(sys.stdin.readline())
beacons = []
for _ in range(n):
    position, power = map(int, sys.stdin.readline().split())
    beacons.append((position, power))

destroyed = 0
last_position = float('inf')

for i in range(n-1, -1, -1):
    position, power = beacons[i]
    if last_position <= position - power:
        destroyed += (power - (last_position - position))
    else:
        destroyed += power
    last_position = position

print(destroyed)
