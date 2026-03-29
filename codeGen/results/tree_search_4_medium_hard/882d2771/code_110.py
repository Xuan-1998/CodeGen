def beautifulGirls():
    t, l, r = map(int, input().split())
    
    dp = [[0] * (r + 1) for _ in range(t + 1)]
    
    trie = {}
    
    def f(n):
        if n == 2:
            return 3
        if n == 3:
            return 5
        if n == 4:
            return 8
        if n not in trie:
            val = min(2 * f((n - 1) // 2) + n, (n + 1) // 2)
            trie[n] = val
        return trie[n]
    
    for i in range(t, -1, -1):
        for j in range(l, r + 1):
            if j == l:
                dp[i][j] = f(j - l + 1)
            else:
                dp[i][j] = min(dp[i-1][k] + dp[0][j-k-1] for k in range(j-l+1))
    
    res = sum(dp[i][r-i] for i in range(t)) % (10**9 + 7)
    
    print(res)

beautifulGirls()
