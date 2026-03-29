def solve():
    T = int(input())
    MOD = 10**9 + 7

    for _ in range(T):
        N, M = map(int, input().split())
        dp = [[0] * (M + 1) for _ in range(N + 1)]

        for i in range(1, N + 1):
            for j in range(i, M + 1):
                if i == 1:
                    dp[i][j] = 1
                else:
                    total_sum = sum(range(j - i + 1))
                    dp[i][j] = (dp[i-1][j-i] + total_sum) % MOD

        print(dp[N][M])

if __name__ == "__main__":
    solve()
