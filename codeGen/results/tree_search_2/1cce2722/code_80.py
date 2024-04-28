def max_points(n):
    a = list(map(int, input().split()))
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if a[i - 1] % 2 == 0:
            delete_0 = dp[i - 1] + (a[i - 1] - 1) if i > 1 else 0
            delete_pm1 = dp[i - 2] + (a[i - 1] - 1) if i > 1 else 0
            dp[i] = max(delete_0, delete_pm1)
        else:
            dp[i] = dp[i - 1]
    
    return dp[n]

n = int(input())
print(max_points(n))
