def max_points_earned(n, a):
    dp = [0] * (n + 1)
    
    for i in range(2, n + 1):
        if i > 2 and a[i-1] == a[i-2] - 1 or a[i-1] == a[i-2] + 1:
            dp[i] = max(dp[i-1], dp[i-3])
        else:
            dp[i] = max(dp[i-1], dp[i-2]) if i > 1 and (a[i-1] != a[i-2] - 1 and a[i-1] != a[i-2] + 1) else 0
    
    return dp[-1]

n = int(input())
a = list(map(int, input().split()))
print(max_points_earned(n, a))
