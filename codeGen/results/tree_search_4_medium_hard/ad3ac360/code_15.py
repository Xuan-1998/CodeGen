===BEGIN CODE===
def min_cuts(s):
    n = len(s)
    
    # Initialize the DP table
    dp = [[False] * n for _ in range(n)]
    
    # Fill in the DP table using a bottom-up approach
    for i in range(n):
        for j in range(i, n):
            if s[i] == s[j]:
                if j - i <= 2:  # Single characters or substrings of length 2 are always palindromes
                    dp[i][j] = True
                else:
                    for k in range(i, j):
                        if s[k] == s[j-k+1]:
                            dp[i][j] = (dp[i][k-1] and dp[k+1][j])
                            break
            else:
                dp[i][j] = False
    
    # Compute the minimum number of cuts
    min_cuts = 0
    for i in range(n):
        for j in range(i, n):
            if not dp[i][j]:
                min_cuts += 1
    
    return min_cuts

# Read input from standard input (stdin)
s = input()

print(min_cuts(s))
