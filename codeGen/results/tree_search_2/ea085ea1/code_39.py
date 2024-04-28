def max_non_overlapping_substrings():
    N = int(input())  # Read the length of each string from stdin

    str1 = input()  # Read the first string from stdin
    str2 = input()  # Read the second string from stdin

    dp = [[0] * (N + 1) for _ in range(N + 1)]  # Initialize the DP table

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[N][N]

print(max_non_overlapping_substrings())  # Print the result to stdout
