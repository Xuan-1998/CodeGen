from collections import defaultdict

def max_common_substrings():
    N = int(input())
    str1 = input().strip()
    str2 = input().strip()

    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if str1[i - 1] == str2[-j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[N][N]

print(max_common_substrings())
