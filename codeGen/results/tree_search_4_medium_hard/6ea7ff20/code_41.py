n = int(input())
p = list(map(int, input().split()))
dp = [[False] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    dp[0][i] = True

for j in range(n+1):
    dp[j][0] = False

for i in range(1, n+1):
    for j in range(1, n+1):
        if p[2*i-1] < p[2*j-1]:
            dp[i][j] = (dp[i-1][j] or any(dp[k][i-1] and dp[j-k][n-j+1] for k in range(min(i, j))))
        else:
            dp[i][j] = False

print("YES" if any(dp[n][j] for j in range(n)) else "NO")
