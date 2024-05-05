import sys

def query_dp(dp, l, r):
    while l < r:
        if dp[l][r-1] == dp[l+1][r]:
            return dp[l][r]
        l += 1
    return dp[l][r]

n, q = map(int, input().split())
dp = [[i+1 for _ in range(n)] for _ in range(n)]

signs = list(input())
for i in range(n):
    if signs[i] == '+':
        signs[i] = -1
    else:
        signs[i] = 1

for i in range(1, n):
    for j in range(i):
        dp[j][i-1] = min(dp[j][i-2]+1, dp[j+1][i])
    if signs[i] == -1:
        dp[0][i-1] = i
    else:
        dp[0][i-1] = 0

for _ in range(q):
    l, r = map(int, input().split())
    print(query_dp(dp, l-1, r-1))
