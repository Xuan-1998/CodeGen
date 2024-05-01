def max_common_substrings(str1, str2):
    N = len(str1)
    dp = [[False] * (N + 1) for _ in range(N + 1)]
    
    res = 0
    for i in range(N):
        for j in range(N):
            if str1[i] == str2[j]:
                dp[i][j] = True
                if i > 0 and j > 0:
                    dp[i][j] = dp[i-1][j-1] or dp[i][j]
    
    for i in range(N):
        for j in range(N):
            if dp[i][j]:
                res += 1
                while j < N and str2[j] == str1[i]:
                    i += 1
                    j += 1
    
    return res

# Input
str1 = input()
str2 = input()

# Solve the problem
print(max_common_substrings(str1, str2))
