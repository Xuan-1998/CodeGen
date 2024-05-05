import sys

# Define constants
MOD = 1000000000

def solve(N, M):
    # Initialize memoization array with zeros
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # Fill in the base case: sum(R[0][k]) <= M
    for j in range(M + 1):
        if sum(range(1, j + 1)) <= M:
            dp[0][j] = 1
        else:
            dp[0][j] = 0

    # Calculate the number of different steady tables for each row and column
    for i in range(N + 1):
        for j in range(1, M + 1):
            if sum(range(i + 1)) <= M - j:
                dp[i][j] = (sum(range(i)) <= M - j) * dp[i-1][j-1]
            else:
                dp[i][j] = 0

    # Return the result modulo MOD
    return sum([dp[N][j] for j in range(M + 1)]) % MOD

# Read input from stdin and process each test case
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(solve(N, M))
