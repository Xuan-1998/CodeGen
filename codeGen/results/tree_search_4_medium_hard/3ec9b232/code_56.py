import sys
from collections import defaultdict

n = int(input())
m = list(map(int, input().split()))

dp = [0] * (n + 1)
dp[0] = 1

counts = defaultdict(int)

for i in range(n):
    counts[m[i]] += 1
    for j in range(i):
        dp[i + 1] = (dp[i + 1] + dp[j] * (n - j)) % (10**9 + 7)
    if m[i] > 0:
        dp[i + 1] = (dp[i + 1] + counts[m[i]]) % (10**9 + 7)

print(dp[-1])
