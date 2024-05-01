def max_common_substrings(str1, str2):
    N = len(str1)
    M = len(str2)

    dp = [[0] * (M + 1) for _ in range(N + 1)]

    max_common = 0

    i, j = 0, 0
    while i <= N and j <= M:
        if str1[i] == str2[j]:
            dp[i][j] = 1 + dp[i - 1][j - 1]
            max_common = max(max_common, dp[i][j])
            i += 1
            j += 1
        elif j > 0:
            j -= 1
        else:
            i += 1

    return max_common


# Read input from stdin
str1 = input().strip()
str2 = input().strip()

# Print the result to stdout
print(max_common_substrings(str1, str2))
