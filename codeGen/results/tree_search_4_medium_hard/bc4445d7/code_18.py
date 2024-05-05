def solve():
    n, = map(int, input().split())
    adj_list = [[] for _ in range(n)]
    k, = map(int, input().split())
    prime_factors = list(map(int, input().split()))
    
    memo = {}
    
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == n-1:
            memo[(i, j)] = 0
            return 0
        
        if j == 0:
            memo[(i, j)] = i
            return i
        
        res = float('inf')
        for p in prime_factors:
            res = min(res, dp(i+1, j-1) + i)
        
        memo[(i, j)] = res
        return res
    
    print(dp(0, n-2) % (10**9 + 7))
