import sys
from bisect import bisect_left

n = int(input())
dp = [0] * n
bns = []

for _ in range(n):
    a, b = map(int, input().split())
    bns.append((a, b))

dp[-1] = 0

for i in reversed(range(n-1)):
    for (a, b) in bns[i+1:]:
        if dp[i+1] < b:
            dp[i] = max(dp[i], b)
            break
    else:
        dp[i] = dp[i+1]

print(max(0, dp[0]))
