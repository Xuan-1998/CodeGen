def find_common_substrings():
    n = int(input())
    str1 = input().strip()
    str2 = input().strip()

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    max_len = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_len = max(max_len, dp[i][j])

    return max_len

print(find_common_substrings())
