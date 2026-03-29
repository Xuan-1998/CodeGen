def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0] * (m+1) for _ in range(10)]
        for j in range(m+1):
            dp[1][j] = 1
        for i in range(2, 11):
            for j in range(1, m+1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[k][j-1] for k in range(1, i+1)) + 1
        print((dp[n][m]) % (10**9 + 7))

solve()
