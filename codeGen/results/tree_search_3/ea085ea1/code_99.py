def maxCommonSubstrCount():
    N = int(input())
    str1 = input().strip()
    str2 = input().strip()

    dp = [[False] * (N + 1) for _ in range(N + 1)]
    max_common_substr_count = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
                max_common_substr_count[i][j] = max_common_substr_count[i - 1][j - 1] + 1
            else:
                if i > j and j > 0:
                    dp[i][j] = False
                elif i == j:
                    dp[i][j] = True
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return max_common_substr_count[N][N]

print(maxCommonSubstrCount())
