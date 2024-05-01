===BEGIN CODE===
def maxCommonSubstrings(str1, str2):
    N = len(str1)
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    for k in range(1, N + 1):
        for i in range(N - k + 1):
            j = i + k
            if str1[i:j] == str2[i:j]:
                dp[i][j] = min(dp[i][k-1], dp[k-1][j]) + 1
    
    return sum(max(row) for row in dp)

str1 = input().strip()
str2 = input().strip()

print(maxCommonSubstrings(str1, str2))

===END CODE===
