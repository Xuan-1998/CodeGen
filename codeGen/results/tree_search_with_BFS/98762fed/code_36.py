MOD = 998244353

def count_valid_matrices(N, M):
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[1][1] = 1

    for n in range(1, N + 1):
        for m in range(1, M + 1):
            if n == 1 and m == 1:
                continue
            if n > 1:
                dp[n][m] += dp[n - 1][m]
                dp[n][m] %= MOD
            if m > 1:
                dp[n][m] += dp[n][m - 1]
                dp[n][m] %= MOD

    return dp[N][M]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    print(count_valid_matrices(N, M))

