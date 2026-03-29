def f(n):
    if n == 1 or n == 2:
        return 0
    
    dp = {i: float('inf') for i in range(1, n+1)}
    
    dp[1] = dp[2] = 0
    
    for i in range(3, n+1):
        for j in range(1, i//2 + 1):
            k = i - j
            if k >= l and f(k) != float('inf'):
                dp[i] = min(dp[i], dp[j] + f(k))
    
    return dp[n]

t, l, r = map(int, input().split())
print(f(t) % (10**9+7))
