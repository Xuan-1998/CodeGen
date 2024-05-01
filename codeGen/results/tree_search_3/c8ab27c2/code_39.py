def find_uncommon_subsequence():
    S = input().strip()
    T = input().strip()

    # Create a 2D array to store the lengths of common subsequences
    dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]

    # Fill up the dynamic programming table
    for i in range(1, len(S) + 1):
        for j in range(1, len(T) + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Return the length of the shortest uncommon subsequence
    return len(S) - dp[-1][-1]

print(find_uncommon_subsequence())
