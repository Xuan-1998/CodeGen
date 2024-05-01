def can_divide(n, m, s):
    dp = {}
    
    def dfs(i, t):
        if (i, t) not in dp:
            if i == 0:
                dp[(i, t)] = t % m == 0
            else:
                dp[(i, t)] = any(dfs(i - j, t - k) for j in range(1 + t // m))
        return dp[(i, t)]
    
    return dfs(n, s)

n, m, s = map(int, input().split())
print(can_divide(n, m, s))
