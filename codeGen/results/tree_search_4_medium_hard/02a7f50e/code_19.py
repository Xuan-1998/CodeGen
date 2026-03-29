import sys

n = int(input())
beacons = []

for _ in range(n):
    a, b = map(int, input().split())
    beacons.append((a, b))

beacons.sort()

dp = [[0] * (max(beacon[1] for beacon in beacons) + 1) for _ in range(len(beacons))]

for i in reversed(range(len(beacons))):
    for j in range(max(beacon[1] for beacon in beacons), -1, -1):
        k = len(beacons) - 1
        while k >= 0 and beacons[k][1] > j:
            k -= 1
        dp[i][j] = min(dp.get(k, [float('inf')] + [k+1] for k in range(i))[min(j, beacons[k][1])], dp[i-1][j])

print(min(dp[-1]))
