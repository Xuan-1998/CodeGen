def isScramble(s1, s2):
    n = len(s1)
    
    # Initialize a 2D array dp with size (n + 1) x (n + 1), filled with False values.
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    
    # Base case: The empty string is scrambled with the empty string.
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for j in range(i, -1, -1):
            if s1[:i] == s2[:j]:
                dp[i][j] = True
            elif i > 1 and j > 1:
                for k in range(1, min(i, j) + 1):
                    if (dp[k][0] and dp[i - k][j]) or (dp[0][k] and dp[i][j - k]):
                        dp[i][j] = True
            else:
                dp[i][j] = s1[:i] == s2[:j]
    
    return dp[n][n]

def isScrambled(s1, s2):
    if len(s1) != len(s2):
        return False
    
    return isScramble(s1, s2)

# Receive inputs from stdin
s1 = input()
s2 = input()

# Print the answer to stdout
print(isScrambled(s1, s2))
