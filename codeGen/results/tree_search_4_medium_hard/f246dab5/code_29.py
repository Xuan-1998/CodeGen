import sys

n = int(sys.stdin.readline().strip())
dp = [[0] * 2 for _ in range(n)]

for i in range(n):
    t_i = int(sys.stdin.readline().strip())
    for j in range(2):
        if i == 0:
            dp[i][j] = t_i
        else:
            if j == 0:
                dp[i][j] = dp[i-1][j] + (t_i - dp[i-1][j])
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][0]) + (t_i - dp[i-1][min(j, 0)])
print(min(dp[-1]))
