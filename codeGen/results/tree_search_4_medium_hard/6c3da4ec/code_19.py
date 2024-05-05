def max_bitwise_or(n, s):
    # Precompute bitwise OR values for single characters (substrings of length 1)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if j - i == 0:  # Empty substring
            return 0

        max_or = 0

        for k in range(i + 1, j + 1):
            or_val = int(s[i:k], 2) | int(s[k:j], 2)
            max_or = max(max_or, dfs(k, j))

        memo[(i, j)] = max_or
        return max_or

    # Initialize DP table with base cases (single characters)
    for i in range(n + 1):
        dp[i][i] = int(s[i], 2)

    # Fill up the DP table using dynamic programming and memoization
    for length in range(1, n // 2 + 1):  # Only need to consider substrings of this length or shorter
        for i in range(n - length):
            j = i + length
            dp[i][j] = dfs(i, j)

    # Find the maximum bitwise OR value across all possible pairs
    max_or = 0
    for i in range(1, n // 2 + 1):  # Only need to consider substrings of this length or shorter
        for j in range(n - i):
            max_or = max(max_or, dp[j][j + i])

    return bin(max_or)[2:].zfill(n).count('1')

n = int(input())
s = input()
print(max_bitwise_or(n, s))
