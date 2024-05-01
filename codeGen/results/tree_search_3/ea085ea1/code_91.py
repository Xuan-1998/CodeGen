import sys

def max_common_substrings(str1, str2):
    n = len(str1)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    max_length = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                length = dp[i][j]
                while length > 0 and (i - length) < n and (j - length) < n:
                    if str1[i - length - 1] != str2[j - length - 1]:
                        break
                    length -= 1
                max_length = max(max_length, length)

    return max_length

str1 = input().strip()
str2 = input().strip()

print(max_common_substrings(str1, str2))
