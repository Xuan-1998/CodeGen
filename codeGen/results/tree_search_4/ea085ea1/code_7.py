import sys

def solve(str1, str2):
    N = len(str1)
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Pre-compute all possible substrings for both strings
    substrings = set()
    for i in range(N):
        for j in range(i, N):
            substrings.add(str1[i:j+1])
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if str1[:i] == str2[:j]:
                dp[i][j] = dp[i-1][j-1] + 1
            elif dp[i-1][j] > 0 and dp[i][j-1] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = 0
    
    # Find the maximum number of common non-overlapping substrings
    max_common_substrings = 0
    for i in range(N, -1, -1):
        for j in range(N, -1, -1):
            if dp[i][j] > max_common_substrings:
                max_common_substrings = dp[i][j]
    
    return max_common_substrings

# Read input from standard input
str1 = input()
str2 = input()

# Print the answer to standard output
print(solve(str1, str2))
