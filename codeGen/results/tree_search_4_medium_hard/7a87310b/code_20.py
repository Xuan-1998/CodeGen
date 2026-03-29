def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        dp = [[0] * (n+1) for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(1, n+1):
            for j in range(i, n+1):
                if i + j == n:
                    dp[i][j] = (i > 0 and j > 0) or (i > 0 and j < n) or (i < n and j > 0) or (i < n and j < n)
                    if dp[i][j]:
                        dp[i][j] += dp[i-1][j-1] + dp[i-1][j]
                    else:
                        dp[i][j] = 0
                elif i > 0 and j > 0:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                elif i > 0 and j < n:
                    dp[i][j] = dp[i-1][j+1] + dp[i-1][j]
                elif i < n and j > 0:
                    dp[i][j] = dp[i+1][j-1] + dp[i+1][j]
                elif i < n and j < n:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]

        print(sum([row[-1] for row in dp]))

solve()
