import sys

def count_steady_tables(N, M):
    dp = [[0] * (M+1) for _ in range(N+1)]

    # Initialize base cases
    for i in range(N+1):
        dp[i][0] = 1
    for j in range(M+1):
        dp[0][j] = 1

    # Fill up the dynamic programming table
    for i in range(1, N+1):
        for j in range(1, M+1):
            if i == 1:
                dp[i][j] = 1
            elif j == 1:
                dp[i][j] = 1
            else:
                # Calculate the number of steady tables of size i x (j-1)
                dp[i][j] = sum(dp[k][j-1] for k in range(i))

    # Return the result modulo 1e9
    return dp[N][M] % int(1e9)

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(count_steady_tables(N, M))
