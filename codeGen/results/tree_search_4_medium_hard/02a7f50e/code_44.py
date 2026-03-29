import sys
from bisect import bisect_left, bisect_right

n = int(input())
max_power = 0
beacons = []

for _ in range(n):
    a, b = map(int, input().split())
    max_power = max(max_power, b)
    beacons.append((a, b))

beacons.sort()

dp = [[sys.maxsize] * (max_power + 1) for _ in range(len(beacons) + 1)]

for i in range(1, len(beacons) + 1):
    a, b = beacons[i - 1]
    for j in range(max_power, b - 1, -1):
        k = bisect_right(beacons, (a - j, sys.maxsize)) - 1
        dp[i][j] = min(dp[i][j], dp[k][b - 1] + 1)

print(min(dp[-1]))
