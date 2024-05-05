def solve(n, m):
    memo = {}
    
    def dp(n, m):
        if (n, m) in memo:
            return memo[(n, m)]
        
        if m == 0:
            return len(str(n))
        
        result = 1 + sum(dp(int(digit), m-1) for digit in str(n))
        memo[(n, m)] = result
        return result
    
    return dp(n, m) % (10**9+7)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(solve(n, m))
