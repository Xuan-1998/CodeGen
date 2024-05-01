from collections import defaultdict

def max_common_substrings(str1, str2):
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = 0
    
    max_len = 0
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if dp[i][j] > max_len and str1[i - dp[i][j]:i] == str2[j - dp[i][j]:j]:
                max_len = dp[i][j]
    
    return max_len

str1 = input().strip()
str2 = input().strip()

print(max_common_substrings(str1, str2))
