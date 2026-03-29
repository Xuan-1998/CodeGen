def alienWords(n, m):
    memo = {}
    
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == 0:
            return 1
        
        res = 0
        if i % 2 == 0:
            res += dp(i-1, m-1) * (n - i//2)
            if i//2 > n:
                res += dp(i//2, m-1) * (n - i//2)
        
        memo[(i, j)] = res
        return res
    
    MOD = 10**9 + 7
    total = 0
    for _ in range(int(input())):
        n, m = map(int, input().split())
        total += dp(n, m) % MOD
    print(total % MOD)

