def solve():
    T = int(input())
    MOD = 10**9 + 7
    
    dp = {}

    def dfs(i, j):
        if (i, j) in dp:
            return dp[(i, j)]
        
        if i == 0:
            return 1
        
        if j == 0:
            return 0
        
        res = 0
        for k in range(j+1):
            if k <= i:
                res += dfs(i-k, j-k)
        
        dp[(i, j)] = res % MOD
        return res

    for _ in range(T):
        N, M = map(int, input().split())
        print(dfs(N, M))
