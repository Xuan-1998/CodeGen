from collections import defaultdict

def max_common_substrings(str1, str2):
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    
    # Initialize the base case: there are no common substrings when starting from the beginning of both strings.
    dp[0][0] = 0
    
    memo = defaultdict(list)
    
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                # If the current characters match, consider the maximum number of common non-overlapping substrings ending at position i-1 in str1 and j-1 in str2, plus 1 (since this new substring is also a common one).
                dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i][j])
                
                # Store the current state to avoid recalculating it.
                memo[dp[i][j]].append((i, j))
    
    # Return the maximum number of common non-overlapping substrings between str1 and str2.
    return max(len(substrings) for substrings in memo.values())

# Receive inputs from stdin
str1 = input()
str2 = input()

print(max_common_substrings(str1, str2))
