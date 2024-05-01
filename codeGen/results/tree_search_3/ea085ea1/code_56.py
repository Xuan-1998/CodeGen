import sys

def find_common_substrings():
    N = int(input())
    str1 = input().strip()
    M = len(str1)
    str2 = input().strip()
    N = len(str2)

    dp = [[-1] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if str2[i - 1] == str1[j - 1]:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j] + 1)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]

print(find_common_substrings())
