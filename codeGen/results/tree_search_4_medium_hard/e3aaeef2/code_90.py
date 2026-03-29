def solve():
    t = int(input())
    MOD = 10**9+7
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, min(i,m)+1):
                if j == 1:
                    dp[i][j] = i
                else:
                    dp[i][j] = min((k+1) + dp[k][j-1] for k in range(i))
        print(dp[n][m]%MOD)

solve()
