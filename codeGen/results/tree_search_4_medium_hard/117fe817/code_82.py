def find_digit_one(n):
    memo = {}
    
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == j:
            return bin(j)[2].count('1')
        
        res = dp(0, j)
        for k in range(i, j+1):
            res += 1 if str(k).endswith('1') else 0
        memo[(i, j)] = res
        return res
    
    total_count = 0
    for i in range(n+1):
        total_count += dp(0, i)
    return total_count

n = int(input())
print(find_digit_one(n))
