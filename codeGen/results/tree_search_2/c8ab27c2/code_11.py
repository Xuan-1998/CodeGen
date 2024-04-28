def shortest_uncommon_subsequence(S, T):
    n = len(S)
    m = len(T)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Initialize the base case
    for i in range(n + 1):
        dp[i][0] = i

    # Fill up the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

    # Find the shortest uncommon subsequence
    result = float('inf')
    for i in range(1, n + 1):
        if dp[i][m] > result:
            break
        j = m
        while j > 0 and dp[i][j] > result:
            j -= 1
        if j == 0:
            result = dp[i][m]

    return result - 1 if result != float('inf') else -1

# Read input from standard input
S = input()
T = input()

print(shortest_uncommon_subsequence(S, T))
