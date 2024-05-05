from collections import defaultdict

T = int(input())
mod = 1000000000
dp = [[0]*2001 for _ in range(2002)]

for _ in range(T):
    N, M = map(int, input().split())
    ans = 0
    for i in range(N+1):
        if i > 0:
            dp[i][M] += dp[i-1][M]
        for j in range(M+1):
            dp[N][j] += dp[N][j]
    for i in range(N, -1, -1):
        for j in range(M+1):
            if j <= M and (i == 0 or j > 0):
                ans = (ans + dp[i-1][M-j]) % mod
    print(ans)
