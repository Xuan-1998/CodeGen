import sys

mod = 10**9 + 7

dp = [[0]*(20) for _ in range(315)]

a, b = map(int, input().split())
for i in range(315):
    if i < b:
        dp[i][b] = (1 << i) ^ a
    else:
        dp[i][b] = (dp[i-1][b>>1] + (1 << i) ^ a) % mod

print(sum([dp[i][b] for i in range(315)]))
