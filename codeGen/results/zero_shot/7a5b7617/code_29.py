import sys

def count_steady_tables(N, M):
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(M + 1):
            if i == 1:
                dp[i][j] = 1
            elif j < M:
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j + 1]) % 1000000000
            else:
                dp[i][j] = dp[i - 1][M]

    return dp[N][M]

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(count_steady_tables(N, M))
