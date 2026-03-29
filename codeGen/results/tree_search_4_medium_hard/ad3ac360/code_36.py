def minCut(s):
    n = len(s)
    
    # Create a 2D table to store whether substrings are palindromes
    dp = [[False] * n for _ in range(n)]
    
    # Initialize the diagonal elements (single characters) as True
    for i in range(n):
        dp[i][i] = True
    
    # Fill the table from top to bottom and left to right
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # Check if characters match and the substring is palindromic
            if s[i] == s[j] and (length == 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
    
    # Initialize min_cuts to n - 1 (minimum number of cuts for a single string)
    min_cuts = n - 1
    
    # Iterate over the table from bottom to top
    for i in range(n):
        # Find the previous position j such that dp[i][j] is True and the number of cuts is minimized
        for j in range(i):
            if dp[j][i]:
                min_cuts = min(min_cuts, j)
    
    return min_cuts

# Test your solution
s = input()
print(minCut(s))
