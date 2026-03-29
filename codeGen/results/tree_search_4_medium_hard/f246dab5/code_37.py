import sys

n = int(sys.stdin.readline())
dp = [[0, 0] for _ in range(n + 1)]

for i in range(1, n + 1):
    t_i = int(sys.stdin.readline())
    dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + (t_i // 90) * 50
    dp[i][1] = min(dp[max(0, i - 90)][1], dp[i-1][1]) + t_i

print(min(dp[n][0], dp[n][1]))
