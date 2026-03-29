n = int(input())
beacons = []
for _ in range(n):
    pos, power = map(int, input().split())
    beacons.append((pos, power))

beacons.sort()

destroyed = 0
max_power = 0

for pos, power in reversed(beacons):
    if power > max_power:
        destroyed += (power - max_power)
        max_power = power

print(destroyed)
