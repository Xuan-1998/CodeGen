def shortestUncommonSubsequence(S, T):
    m, n = len(S), len(T)
    dp = [[False] * (n+1) for _ in range(m+1)]

    # Initialize base cases
    for i in range(m+1):
        if i == 0:
            dp[i][0] = True

    for j in range(n+1):
        if j == 0:
            dp[0][j] = False

    # Fill up the DP table
    for i in range(1, m+1):
        for j in range(1, n+1):
            if S[i-1] == T[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = not (S[i-1] in T[:j] or T[j-1] in S[:i])

    # Find the length of the shortest uncommon subsequence
    for i in range(m, -1, -1):
        if all(not dp[i][j] for j in range(n+1)):
            return m-i

    return -1

# Test cases
S = input()
T = input()

print(shortestUncommonSubsequence(S, T))
