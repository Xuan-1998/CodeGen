def max_common_substrings(str1, str2):
    n = len(str1)
    m = len(str2)
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    max_count = 0
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_count = max(max_count, dp[i][j])
    
    return max_count

str1 = input()
str2 = input()

print(max_common_substrings(str1, str2))
