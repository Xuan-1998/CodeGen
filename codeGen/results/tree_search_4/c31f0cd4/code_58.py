def distinct_sum(N):
    dp = {}
    for s in range(1, N+2):
        dp[s] = []
    
    def dfs(i, s):
        if (i, s) in dp:
            return dp[(i, s)]
        
        result = set()
        for j in range(i+1):
            subset_sums = dfs(j, 0)
            for ss in subset_sums:
                dp[s].append(ss + a[j])
        
        dp[(i, s)] = list(set(dp[s]))
        return dp[(i, s)]
    
    a = [int(x) for x in input().split()]
    N = len(a)
    sums = set()
    for i in range(N):
        dfs(i, 0)
    
    print(' '.join(map(str, sorted(list(set([s for ss in dp.values() for s in ss]))))))
