from sys import stdin

m = int(stdin.readline())
dp = [[float('inf')] * (n-m+1) for _ in range(m)]

for i in range(n-m+1):
    dp[0][i] = c_new_section * (i + 1)

for i in range(1, m):
    for j in range(n-m+1):
        if j == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i-1][j-1] + c_s_j, dp[1][i][j-1] + c_new_section)

print(dp[m-1][n-m])
