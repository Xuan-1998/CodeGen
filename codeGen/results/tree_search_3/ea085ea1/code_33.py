def max_common_substrings(str1, str2):
    memo = {}
    
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == 0 or j == 0:
            return 0
        
        k = 0
        while k < min(i, j) and str1[i - 1] == str2[j - 1]:
            k += 1
            i -= 1
            j -= 1
        
        memo[(i, j)] = max(dp(i, j - 1), dp(i - 1, j)) + (k > 0)
        
        return memo[(i, j)]
    
    return dp(len(str1), len(str2))
