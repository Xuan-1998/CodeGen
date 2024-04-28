def findShortestUncommonSubsequence(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the base case: an empty subsequence is always uncommon
    for i in range(m + 1):
        dp[i][0] = -1

    for j in range(n + 1):
        dp[0][j] = -1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i-1] != T[j-1]:
                # If the characters don't match, consider including this character
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                # If the characters do match, we can't include this character in our subsequence
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])

    return -dp[m][n] - 1

# Example usage:
S = input()
T = input()

print(findShortestUncommonSubsequence(S, T))
