def shortest_uncommon_subsequence(S, T):
    n = len(S)
    m = len(T)

    # Initialize dp table with zeros
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill dp table using dynamic programming
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Calculate the maximum difference as the shortest uncommon subsequence
    return n + m - (dp[n][m] * 2)

# Receive inputs from stdin
S = input().strip()
T = input().strip()

# Print the answer to stdout
print(shortest_uncommon_subsequence(S, T))
