import sys

# Read input
T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))

    # Initialize memoization table
    dp = [[0] * (C + 1) for _ in range(C + 2)]

    # Base cases
    dp[0][j] = 1
    dp[C + 1][j] = 0

    # Fill up the memoization table
    for i in range(1, C + 1):
        for j in range(min(i, C), -1, -1):
            dp[i][j] = (dp[max(0, i - 1)][min(C, j)] * sum(U[k] <= j for k in range(N)) +
                        dp[max(0, i - 1)][min(C, j)] * sum(L[k] <= j for k in range(M)))

    # Print the result
    print(' '.join(map(str, dp[C])))
