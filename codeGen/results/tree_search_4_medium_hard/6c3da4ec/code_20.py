dp = [[0] * (n + 1) for _ in range(n)]

for i in range(n):
    dp[i][0] = int(s[:i+1], 2)
    
for i in range(1, n):
    for j in range(i, n):
        if j - i == 1:
            dp[i][j+1] = dp[i-1][j]
        else:
            max_or = 0
            for k in range(i, j + 1):
                max_or = max(max_or, dp[i][k] | dp[k][j+1])
            dp[i][j+1] = max_or

print(bin(max(dp[0][n-1]))[2:].zfill(n).lstrip('0'))
