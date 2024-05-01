def max_common_substrings(str1, str2):
    N = len(str1)
    dp = [[0] * (N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, N+1):
            if str1[i-1] == str2[j-1]:
                k = 1
                while i-k > 0 and j-k > 0 and str1[i-k:i] == str2[j-k:j]:
                    k += 1
                dp[i][j] = max(dp[i-k][j-k] + 1, dp[i-1][j-1])
            else:
                dp[i][j] = dp[i-1][j-1]

    return max(dp[N][i] for i in range(N))

str1 = input()
str2 = input()

print(max_common_substrings(str1, str2))
