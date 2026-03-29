# Code starts here
n = int(input())
dp = [float('inf')] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    last_occurrence = -1
    for j in range(n, -1, -1):
        if dp[i - 1].index(min(dp[i - 1])) == ord(input().strip()) - ord('a'):
            last_occurrence = j
        dp[i][j] = min(dp[i][j], dp[i - 1][last_occurrence] + n - i)

print(-1) if dp[n][0] == float('inf') else print(min(dp[n]))
