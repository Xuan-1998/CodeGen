import sys

n = int(sys.stdin.readline())
beacons = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    beacons.append((a, b))

# Sort beacons by position
beacons.sort()

kill_ranges = [0] * n
total_destroyed = 0

for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if beacons[j][0] > beacons[i][0]:
            kill_ranges[i] += 1
        else:
            break
    total_destroyed += kill_ranges[i]
    print(kill_ranges[i], end=' ')
print()
