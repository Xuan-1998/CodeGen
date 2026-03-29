def solve(n, m):
    MOD = 10**9 + 7
    dp = [[0] * (m + 1) for _ in range(11)]

    # Base case: dp[0][j] = 1 for all j
    for j in range(m + 1):
        dp[0][j] = 1

    # Fill up the dynamic programming table from bottom to top
    for i in range(1, n + 1):
        for j in range(min(i, m) + 1):
            if i % 10 % 2 == 0:  # Last digit is even
                dp[i][j] = min(dp[(i // 10)][j - 1], dp[(i // 10)][j]) + 1
            else:  # Last digit is odd
                dp[i][j] = min(dp[(i // 10)][j], dp[(i // 10)][j])

    return dp[n][m] % MOD

# Read input from stdin and print the answer to stdout
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(solve(n, m))
