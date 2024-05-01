import sys

def find_max_common_substrings():
    N = int(input())
    str1, str2 = input().split()  # assume space-separated input

    dp = [[0] * (N + 1) for _ in range(N + 1)]
    max_length = max(len(str1), len(str2))

    for i in range(1, N + 1):
        for k in range(min(i, max_length), -1, -1):
            if str1[i - k:i + 1] == str2[i - k:i + 1]:
                dp[i][k] = dp[i - 1][k - 1] + 1
            else:
                dp[i][k] = max(dp[i - 1][k], dp[i][k - 1])

    return dp[N][max_length]

print(find_max_common_substrings())
