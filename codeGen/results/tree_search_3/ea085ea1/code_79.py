===BEGIN CODE===
def find_common_substrings():
    str1 = input().strip()
    str2 = input().strip()

    N = len(str1)
    right_str1_pos = 0
    max_common_substrings = 0

    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_common_substrings = max(max_common_substrings, dp[i][j])
            else:
                dp[i][j] = 0

    return max_common_substrings

print(find_common_substrings())
