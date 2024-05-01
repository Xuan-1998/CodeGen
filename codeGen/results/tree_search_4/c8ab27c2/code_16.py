def shortest_uncommon_subsequence(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize base cases
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(m + 1):
        dp[i][0] = i

    # Fill up the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                if T.count(S[i - 1]) == 0:  # If this is the first occurrence of char S[i-1] in S and it's not present in T
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])

    # Return the minimum length of a subsequence that ends with character S[m-1] and T[n-1]
    return dp[m][n] - 1

# Read input from stdin
S, T = input().split()

# Print the output to stdout
print(shortest_uncommon_subsequence(S, T))
