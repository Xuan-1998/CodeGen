from collections import defaultdict

def common_substrings(str1, str2):
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])
    
    max_length = 0
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i:i + dp[i + 1][j + 1]].count(str1[i]) == len(str1[i:i + dp[i + 1][j + 1]]):
                max_length = max(max_length, dp[i + 1][j + 1])
    
    return sum(1 for k in range(1, max_length + 1) if str1.count(str1[:k]) > 0 and str2.count(str1[:k]) > 0)

str1 = input()
str2 = input()

print(common_substrings(str1, str2))
