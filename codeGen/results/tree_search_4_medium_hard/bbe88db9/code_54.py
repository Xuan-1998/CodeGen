n = int(input())
p = list(map(int, input().split()))
dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(2, n+1):
    for j in range(1, min(i+1, n+1)):
        if p[i-1] == j:
            dp[i][j] = dp[i-1][i] + 1
        elif dp[i-1][j]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = 0

print(dp[1][n+1] % (10**9 + 7))
