import sys

def uncommon_subsequences_length(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return m - dp[m][n]

# Read input from standard input.
S, T = map(str.strip, open().readlines())

# Print the output to standard output.
print(uncommon_subsequences_length(S, T))
