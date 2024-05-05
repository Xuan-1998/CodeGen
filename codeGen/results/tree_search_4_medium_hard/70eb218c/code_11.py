def min_operations(n, x):
    memo = {}
    
    def dp(k, l):
        if (k, l) in memo:
            return memo[(k, l)]
        
        if k == l:
            return 0
        
        last_digit = (x % 10)
        new_x = 10 * x // 10 + last_digit
        new_l = l - 1
        
        if last_digit != 0:
            res = dp(k+1-1, new_l) + 1
        else:
            res = -1
        
        memo[(k, l)] = res
        return res
    
    return dp(0, n)
