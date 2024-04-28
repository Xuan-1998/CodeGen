def find_shortest_uncommon_subsequence():
    S = input().strip()
    T = input().strip()

    # Initialize the dynamic programming table
    dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]

    # Fill the table using dynamic programming
    for i in range(1, len(S) + 1):
        for j in range(1, len(T) + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])

    # Find the shortest uncommon subsequence by considering the characters in S and T simultaneously
    shortest_uncommon_subsequence_length = len(S)
    for i in range(len(S)):
        for j in range(len(T)):
            if S[i] != T[j]:
                shortest_uncommon_subsequence_length = min(shortest_uncommon_subsequence_length, len(S) - i)

    return shortest_uncommon_subsequence_length
