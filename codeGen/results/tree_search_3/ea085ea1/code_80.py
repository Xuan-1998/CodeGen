def find_max_common_substrings(str1, str2):
    N = len(str1)
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    max_count = 0

    # Initialize the base case: when one of the positions reaches the end of its respective string
    for i in range(N + 1):
        for j in range(N + 1):
            if i == N or j == N:
                dp[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_count = max(max_count, dp[i][j])
            else:
                dp[i][j] = 0

    return max_count

# Read input from stdin
str1 = input().strip()
str2 = input().strip()

# Calculate and print the maximum number of common non-overlapping substrings
max_common_substrings = find_max_common_substrings(str1, str2)
print(max_common_substrings)
