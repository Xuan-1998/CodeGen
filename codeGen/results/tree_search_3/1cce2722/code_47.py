def max_points(a):
    n = len(a)
    k = sum(1 for x in a if x % 2 == 0) // 2
    
    dp = [[0] * (k + 1) for _ in range(n)]
    
    for i in range(k + 1):
        dp[0][i] = i
    
    for i in range(1, n):
        for k in range(min(i, k) + 1):
            if a[i] % 2 == 0:
                dp[i][k] = max(dp[i-1][k], dp[i-1][min(k, (a[i] // 2 - 1))])
            else:
                dp[i][k] = max(dp[i-1][k], dp[i-1][min(k, a[i])])
    
    return dp[-1][-1]

n = int(input())
a = list(map(int, input().split()))
print(max_points(a))
