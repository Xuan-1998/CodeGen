def solve():
    T = int(input())
    MOD = 1000000000

    for _ in range(T):
        N, M = map(int, input().split())

        dp = [[1] * (M + 1) for _ in range(N + 1)]

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                dp[i][j] = dp[i-1][j] + ((i > 1) and dp[i-1][j-1] * j)

        print(dp[N-1][M-1] % MOD)

if __name__ == "__main__":
    solve()
