from collections import defaultdict

def max_common_substrings(str1, str2):
    N = len(str1)
    dp = [[0] * (N+1) for _ in range(N+1)]
    
    # Initialize the base case values
    memo = defaultdict(int)
    for i in range(N+1):
        dp[i][0] = 0
        dp[0][i] = 0
    
    # Fill up the dp table using dynamic programming with memoization
    for i in range(1, N+1):
        for j in range(1, N+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Return the maximum value in the last row of the dp table as the result
    return dp[N-1][-1]

# Read input from standard input
str1, str2 = input().split()

# Print the output to standard output
print(max_common_substrings(str1, str2))
