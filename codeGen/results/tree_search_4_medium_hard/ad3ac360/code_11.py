def min_cuts(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    # Initialize the table by setting dp[i][i] to 1 for all i, 
    # since a single-character substring is always a palindrome.
    for i in range(n):
        dp[i][i] = 1
    
    # Fill in the table using bottom-up tabulation:
    for j in range(2, n):
        for i in range(n - j):
            if s[i] == s[i + j]:  # Check if first and last characters are the same
                if j < 3:  # Single character or two characters that are the same are palindromes
                    dp[i][i + j] = 1
                else:
                    dp[i][i + j] = dp[i + 1][i + j - 1]  # Check if substring is palindrome without first and last characters
            else:
                min_cuts = j - i + 1
                for k in range(i, i + j):
                    if dp[i][k - 1] and dp[k + 1][j]:
                        min_cuts = min(min_cuts, k - i + 1)
                dp[i][i + j] = min_cuts
    
    # Return the value of dp[0][n-1], which represents the minimum number of cuts required for palindrome partitioning.
    return sum(dp[i][j] - 1 for i in range(n) for j in range(i, n)) - 1

# Read input string from standard input
s = input()

print(min_cuts(s))
