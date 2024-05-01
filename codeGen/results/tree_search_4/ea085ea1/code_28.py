import sys

def max_common_substrings():
    N = int(input())
    str1, str2 = input().split()[:N], input().split()[:N]

    dp = [[-1] * (N + 1) for _ in range(N + 1)]

    for i in range(N + 1):
        for j in range(N + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                min_len = min(i, j)
                for k in range(min_len):
                    if str1[i - 1] == str2[j - 1]:
                        dp[i][j] = max(dp[i][j], dp[i - 1 - k][j - 1 - k] + 1)
                        break

    return dp[N][N]

print(max_common_substrings())
