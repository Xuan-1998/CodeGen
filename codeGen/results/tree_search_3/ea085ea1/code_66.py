from collections import defaultdict

def find_common_substrings():
    str1, str2 = input().split()
    N = len(str1)

    dp = [[0] * (N + 1) for _ in range(N + 1)]

    max_len = 0
    for i in range(N):
        for j in range(N):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_len = max(max_len, dp[i][j])

    return max_len

print(find_common_substrings())
