import sys

def min_destroyed_beacons(n):
    # Read input
    beacons = []
    for _ in range(n):
        position, power = map(int, sys.stdin.readline().split())
        beacons.append((position, power))

    # Sort beacons by position and then by power level (in descending order)
    beacons.sort(key=lambda x: (x[0], -x[1]))

    destroyed_beacons = 0
    for i in range(n):
        position, power = beacons[i]
        while i > 0 and beacons[i-1][0] < position - power:
            destroyed_beacons += 1
            i -= 1

    return destroyed_beacons + 1

n = int(sys.stdin.readline())
print(min_destroyed_beacons(n))
