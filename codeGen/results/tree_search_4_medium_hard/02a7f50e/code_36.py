code
import sys

n = int(sys.stdin.readline())
beacons = [(0, 0)] * n
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    beacons[i] = (a, b)

dp = [[0] * len(beacons) for _ in range(len(beacons))]

for i in range(1, len(beacons)):
    for j in range(i + 1):
        if beacons[j][1] >= beacons[i][1]:
            dp[i][j] = dp[i - 1][j]
        else:
            rightmost_active = None
            for k in range(j, i + 1):
                if (rightmost_active is None or beacons[k][0] > rightmost_active[0]) and beacons[k][1] < beacons[i][1]:
                    rightmost_active = (k, beacons[k][1])
            if rightmost_active is not None:
                destroyed = rightmost_active[0] - j + 1
                dp[i][j] = min(dp[i - 1][j], dp[rightmost_active[0] - 1][rightmost_active[0]] + destroyed)
            else:
                dp[i][j] = dp[i - 1][j]

print(min([dp[-1][i] for i in range(len(beacons))]))
