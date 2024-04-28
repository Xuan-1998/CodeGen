def shortest_uncommon_subsequence(S, T):
    n = len(S)
    m = len(T)

    # Create a memoization dictionary to store the results of subproblems
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill up the first row and column with 1s, since an empty string is always a subsequence
    for i in range(n + 1):
        dp[i][0] = 1
    for j in range(m + 1):
        dp[0][j] = 1

    # Compute the lengths of common subsequences using dynamic programming
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S[i - 1] != T[j - 1]:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = dp[i - 1][j - 1]

    # Find the minimum length of an uncommon subsequence
    min_length = n
    for i in range(n + 1):
        if dp[i][m] == 1:
            min_length = min(min_length, i)

    return min_length if min_length != n else -1

# Receive input from stdin and print the output to stdout
S = input()
T = input()
print(shortest_uncommon_subsequence(S, T))
