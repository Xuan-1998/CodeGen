import sys

def max_common_substrings(str1, str2):
    N = len(str1)
    dp = [[-1] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = max(0, dp[i - 1][j], dp[i][j - 1])

    max_count = 0
    for i in range(N, -1, -1):
        for j in range(N, -1, -1):
            if dp[i][j] > 0:
                max_count += 1
                break

    return max_count

str1 = input().strip()
str2 = input().strip()

print(max_common_substrings(str1, str2))
