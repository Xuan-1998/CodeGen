def min_cuts(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    # Base cases: single-character and empty strings are always palindromic
    for i in range(n):
        dp[i][i] = True
    
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j]:  # Check if the middle character is the same as the first and last characters
                dp[i][j] = (length > 2) or dp[i+1][j-1]
            else:
                left_palindromic = False
                right_palindromic = False
                
                for k in range(i, j):
                    if s[i] == s[k]:  # Check if the middle character is the same as the first and last characters
                        left_palindromic = True
                        break
                    
                    if dp[i][k-1] and dp[k+1][j]:
                        left_palindromic = True
                        right_palindromic = True
                        break
                
                dp[i][j] = (left_palindromic or i > 0) and (right_palindromic or j < n-1)
    
    # Find the minimum number of cuts needed for palindrome partitioning
    min_cuts = float('inf')
    for i in range(n):
        if not dp[0][i]:
            min_cuts = min(min_cuts, i+1)
    
    return min_cuts - 1  # Subtract 1 because we're counting the number of cuts

s = input()
print(min_cuts(s))
