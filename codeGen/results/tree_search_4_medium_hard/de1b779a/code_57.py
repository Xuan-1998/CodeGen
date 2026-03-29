import sys

# Read input
n, m, c0, d0 = map(int, input().split())
c = [0] + list(map(int, input().split()))
d = [0] + list(map(int, input().split()))

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(m+1):
        if j == 0:
            dp[i][j] = d0
        elif i < c[j]:
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = max(dp[i-c[j]][j-1], d[j])

# Print the maximum profit
print(dp[-1][-1])
