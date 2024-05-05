def count_digit_ones(k, n):
    memo = {}
    
    def dp(k, n):
        if (k, n) in memo:
            return memo[(k, n)]
        
        if n < 10**k:
            return 0
        
        result = dp(k-1, n//10)
        result += n%10 == 1
        memo[(k, n)] = result
        return result
    
    return dp(9, int(input()))

print(count_digit_ones(9, int(input())))
