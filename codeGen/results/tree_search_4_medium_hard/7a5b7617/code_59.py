def solve():
    N, M = [int(x) for x in input().split()]
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i == 1:
                dp[i][j] = 1
            elif j <= sum(range(i)):
                dp[i][j] = (dp[i-1][sum(range(i)) - (j-1))] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    print(dp[N][M])

if __name__ == "__main__":
    solve()
