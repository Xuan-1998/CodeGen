### BEGIN CODE BLOCK

def max_common_substrings(str1, str2):
    N = len(str1)
    M = len(str2)

    # Initialize the dynamic programming table
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            # Iterate through all possible substrings within the sliding window [i-j]
            for k in range(i - j + 1):  # Consider substrings of length j-i+1
                substr = str1[k:i]  # Extract the substring from str1
                if substr == str2[:j]:  # Check if the substring is common in both strings
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)  # Update dp[i][j]
                    break  # Break out of the inner loop since we've found a new non-overlapping common substring

    return dp[N][M]

### END CODE BLOCK
