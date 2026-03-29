def min_f(a):
    n = len(a)
    dp = [[0] * (2 * s + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = a[i]
        
    for i in range(1, n):
        for j in range(1, 2 * s + 1):
            dp[i][j] = min(dp[i - 1][max(0, j - a[i])] + dp[i - 1][min(j, 2 * s)], 
                           dp[i][j - a[i]] + dp[i - 1][j - a[i]])
    
    return dp[n][-1]

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_f(a))
