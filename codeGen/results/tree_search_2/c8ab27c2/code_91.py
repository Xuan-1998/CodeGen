def minUncommonLength(S, T):
    m, n = len(S), len(T)
    
    # Create a 2D table to store the length of the shortest uncommon subsequence
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the base case: all subsequences are of length 0
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
    
    # Fill up the table using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] != T[j - 1]:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
            else:
                dp[i][j] = dp[i - 1][j - 1]
    
    # The answer is the minimum value in the last row of the table
    return min(dp[m])

S = input().strip()
T = input().strip()

print(minUncommonLength(S, T))
