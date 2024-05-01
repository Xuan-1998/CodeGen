def max_common_substrings(str1, str2):
    N = len(str1)
    dp = [[0] * (N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, N+1):
            if str1[i-1] == str2[j-1]:
                if j == 1:
                    dp[i][j] = dp[i-1][j] + 1
                else:
                    dp[i][j] = max(dp[i-1][k] + 1 for k in range(max(0, j-len(str2[:j])), min(i, j)) if str1[:i] == str2[:k+1])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[N][N]

# Read input strings from stdin
str1 = input()
str2 = input()

print(max_common_substrings(str1, str2))
