def common_substrings(str1, str2):
    N = len(str1)
    memo = {}
    
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == 0 or j == 0:
            return 1
        
        if str1[i-1] != str2[j-1]:
            memo[(i, j)] = max(dp(i-1, j), dp(i, j-1))
        else:
            memo[(i, j)] = 1 + dp(i-1, j-1)
        
        return memo[(i, j)]
    
    result = 0
    for i in range(N):
        for j in range(N):
            result = max(result, dp(i, j))
    
    print(result)

str1 = input()
str2 = input()

common_substrings(str1, str2)
