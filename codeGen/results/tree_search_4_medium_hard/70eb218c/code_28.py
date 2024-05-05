def min_operations(n, x):
    dp = [[float('inf')] * (10 ** n) for _ in range(n + 1)]
    
    def dfs(i, x):
        if i < 0:
            return float('inf')
        if dp[i][x] != float('inf'):
            return dp[i][x]
        
        result = float('inf')
        while x > 0:
            last_digit = x % 10
            if last_digit == 0 and len(str(x)) >= i:
                result = min(result, dfs(i - 1, x // 10))
            elif last_digit != 0:
                result = min(result, dfs(i - 1, x * last_digit))
            x //= 10
        
        dp[i][x] = result
        return result
    
    for i in range(n + 1):
        if x < 10 ** i:
            return -1
    return dfs(n, x)

n, x = map(int, input().split())
print(min_operations(n, x))
