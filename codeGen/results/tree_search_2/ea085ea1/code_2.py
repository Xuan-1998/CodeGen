def max_common_substrings(str1, str2):
    n = len(str1)
    m = len(str2)

    # Initialize the DP array with zeros
    dp = [[[0] * (m+1) for _ in range(n+1)] for _ in range(n+1)]

    # Fill up the first row and column of the DP array
    for i in range(n):
        for j in range(m):
            if str1[i] == str2[j]:
                dp[n-1][i][j] = 1
            else:
                break

    # Calculate the maximum number of common non-overlapping substrings
    max_count = 0
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if str1[i] == str2[j]:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + 1
                max_count = max(max_count, dp[i][j])

    return max_count

# Read the input strings from standard input
str1 = input()
str2 = input()

# Calculate and print the maximum number of common non-overlapping substrings
print(max_common_substrings(str1, str2))
