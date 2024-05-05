import sys

def count_steady_tables(N, M):
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][j] = 1 for each column j]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            # Calculate the number of different steady tables of size i x j
            dp[i][j] = sum(dp[k][j - 1] * min(j, k) for k in range(i))
    return dp[N][M]

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(count_steady_tables(N, M) % 1000000000)
