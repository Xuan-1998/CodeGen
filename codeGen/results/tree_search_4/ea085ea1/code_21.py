from collections import defaultdict

def max_common_substrings(str1, str2):
    n = len(str1)
    m = len(str2)

    # Create a dictionary to store the count of each substring in str1
    str1_count = defaultdict(int)
    for i in range(n):
        for j in range(i+1, n+1):
            substr = str1[i:j]
            str1_count[substr] += 1

    # Initialize the dp table with zeros
    dp = [[0] * (m+1) for _ in range(n+1)]

    # Fill up the base case where the maximum number of common non-overlapping substrings is 0 for any length
    for i in range(1, n+1):
        dp[i][i] = 1

    # Calculate the maximum number of common non-overlapping substrings
    for k in range(2, n+1):
        for j in range(m-k+1):
            for i in range(n-k+1):
                if str1[i:i+k] == str2[j:j+k]:
                    dp[i][j+k-1] = max(dp[i][j+k-1], dp[i+k-1][j+k-1] + 1)

    # Return the maximum number of common non-overlapping substrings
    return dp[0][m-1]

# Read input from stdin
str1 = input().strip()
str2 = input().strip()

# Calculate and print the result
print(max_common_substrings(str1, str2))
