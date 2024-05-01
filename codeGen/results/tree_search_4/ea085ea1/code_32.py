def find_max_common_substrings(str1, str2):
    N = len(str1)
    dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]

    for k in range(1, N + 1):
        for i in range(N - k + 1):
            j = i + k
            for l in range(1, k + 1):
                if str1[i:i+l] == str2[j-j+l:j]:
                    dp[k][j][l] = max(dp[k-1][i][l-1], dp[k-1][j][l-1]) + 1

    return max(max(map(max, dp)))

# Read input from standard input
str1 = input()
str2 = input()

# Calculate the maximum number of common non-overlapping substrings
max_common_substrings = find_max_common_substrings(str1, str2)

print(max_common_substrings)
