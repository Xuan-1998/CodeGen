def solve():
    T = int(input())
    MOD = 10**9 + 7

    for _ in range(T):
        N, M = map(int, input().split())
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        cum_sum = [[0] * (M + 1) for _ in range(N + 1)]
        row_sum = [0] * (N + 1)

        # Base case: all cells are filled with non-negative integers
        for i in range(1, N + 1):
            row_sum[i] = row_sum[i - 1] + M

        for i in range(N - 1, 0, -1):
            for j in range(M - 1, -1, -1):
                for k in range(min(j + 1, M), 0, -1):
                    if (row_sum[i] - row_sum[i - 1]) >= cum_sum[i - 1][j - k]:
                        dp[i][j] += dp[i - 1][j - k]
                        break
                else:
                    dp[i][j] = 0

        for i in range(N):
            cum_sum[i][M] = row_sum[i]

        result = sum(dp[N - 1])
        print(result % MOD)

if __name__ == "__main__":
    solve()
