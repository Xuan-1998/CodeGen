from bisect import bisect_left, bisect_right
import sys

n = int(input())
beacons = []
for _ in range(n):
    a, b = map(int, input().split())
    beacons.append((a, -b))  # negative power level for sorting
beacons.sort()

dp = [0] * (n + 1)
memo = {}

def query(a, b):
    if (a, b) in memo:
        return memo[(a, b)]
    i = bisect_right(beacons, a) - 1
    j = bisect_left(beacons, a + (b // (-beacons[i][1]) - 1))
    dp[j] = min(dp[i], 1 + max(0, (b - beacons[i][1]) // (-beacons[j-1][1]) - 1)) if i >= 0 else 1
    memo[(a, b)] = dp[j]
    return dp[j]

print(query(beacons[-1][0] + (beacons[-2][1] // (-beacons[-1][1])) - 1, beacons[-1][1]))
