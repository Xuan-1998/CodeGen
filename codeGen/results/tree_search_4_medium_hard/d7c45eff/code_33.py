code
n, k = map(int, input().split())
s = input()

dp = [["" for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = s[:i]

for j in range(1, min(i+1, k+1) for i in range(n+1)):
        if s[i-1] <= s[j-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j-1]

print(dp[n][k])
