import sys

n, k = map(int, input().split())
s = input()

dp = [["" for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(k+1):
        if j == 0:
            dp[i][j] = ""
        elif j == 1:
            dp[i][j] = s[:i]
        else:
            delete_str = dp[i-1][j-1]
            dup_str = dp[i][j-1]
            dp[i][j] = min(delete_str, dup_str)

print(dp[n][k])
