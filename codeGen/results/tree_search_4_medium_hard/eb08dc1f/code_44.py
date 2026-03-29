def count_blocks(n):
    MOD = 998244353
    dp = [[0] * (n + 1) for _ in range(10)]
    
    def dfs(i, j, pos):
        if i > n:
            return 0
        
        if pos < 10 and (i == n or num[pos] != j):
            l = i - pos
            dp[ord(str(j))][l] += 1
            return 1
        
        pos += 1
        res = dfs(i, j, pos)
        
        if res:
            for k in range(10):
                if k == j and dp[ord(str(k))][res]:
                    break
            else:
                l = i - pos + 1
                dp[ord(str(j))][l] += 1
        
        return res
    
    num = [int(i) for i in f"{10**n-1:0>{n}}"]
    res = []
    
    for j in range(10):
        dfs(n, j, 0)
        res.append(sum(dp[ord(str(j))]) % MOD)
    
    return ' '.join(map(str, res))
