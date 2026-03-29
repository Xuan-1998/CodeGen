k, n = map(int, input().split())
s = input()

dp = [[[] for _ in range(k+1)] for _ in range(n+1)]

for i in range(n+1):
    for j in range(k+1):
        if j == 0:
            dp[i][j] = ""
        elif i > 0 and j <= n:
            min_str = dp[i-1][j-1]
            if s[i-1] <= min_str[-1]:
                dp[i][j] = s[:i-1] + min_str
            else:
                dp[i][j] = dp[i][j-1]
        elif k > n:
            dp[i][j] = s * (k // n) + s[:k % n]

print(dp[n][k])
