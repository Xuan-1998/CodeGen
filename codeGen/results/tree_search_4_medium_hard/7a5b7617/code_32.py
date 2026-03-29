from collections import defaultdict

def steady_tables(N, M):
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # Base case: only one way to fill the last row with zeros
    dp[N][0] = 1

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            # Case 1: current cell is not part of any sum
            if j > i:
                dp[i][j] = dp[i - 1][0] * (M - j + 1)

            # Case 2: current cell is part of a sum
            else:
                for k in range(1, min(i, j) + 1):
                    dp[i][j] += dp[i - 1][k]

    return dp[N][M] % (10**9 + 7)

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(steady_tables(N, M))
