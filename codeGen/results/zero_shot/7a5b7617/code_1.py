import sys

def count_steady_tables(n, m):
    MOD = 1000000000
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base case: There is only one way to create a steady table of size 0 x j.
    for j in range(m + 1):
        dp[0][j] = 1

    # Fill up the dynamic programming table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1:
                # For the first row, we can create a steady table by filling it with any non-negative integer.
                dp[i][j] = (m + 1) % MOD
            elif i == 2:
                # For the second row, we need to ensure that the sum of elements in the second row is not less than the sum of elements in the first row.
                dp[i][j] = min((m + 1), dp[i - 1][j]) % MOD
            else:
                # For rows beyond the second row, we need to ensure that the sum of elements in each row is not less than the sum of elements in the previous row.
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) % MOD

    return dp[n][m]

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    print(count_steady_tables(n, m))
