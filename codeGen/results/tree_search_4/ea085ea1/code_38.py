def maxCommonSubstrings(str1, str2):
    N = len(str1)
    M = len(str2)

    dp = [[[0] * (M+1) for _ in range(N+1)] for _ in range(N+1)]

    for i in range(N+1):
        for j in range(M+1):
            if i == 0 or j == 0:
                continue
            for k in range(min(i+1, j+1)):
                if str1[i-k] == str2[j-k]:
                    dp[i][j][k] = max(dp[i-1][j-1][k], dp[i-1][j-1][k-1] + 1)
                else:
                    dp[i][j][k] = dp[i-1][j-1][k]
    return dp[N][M][0]

# Read input from stdin
str1 = input().strip()
str2 = input().strip()

# Compute and print the result
result = maxCommonSubstrings(str1, str2)
print(result)
