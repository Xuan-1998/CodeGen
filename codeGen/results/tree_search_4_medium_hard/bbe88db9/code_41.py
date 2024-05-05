import sys; sys.setrecursionlimit(10000)
n = int(input())
dp = [[0, 0] for _ in range(n+1)]
p = list(map(int, input().split()))
dp[1][0] = 0

for i in range(2, n+1):
    if p[i-1] == i:
        dp[i][1] = 1
    else:
        dp[i][0] = min(dp[p[i-1]][k] for k in [0, 1]) + 1
        if dp[i-1][0] % 2 != 0:  # If ceiling has odd number of crosses
            dp[i][1] = dp[i][0] + (dp[i-1][1] - dp[i-1][0]) % 2
        else:
            dp[i][1] = dp[i][0]

print(min(dp[n+1]))
