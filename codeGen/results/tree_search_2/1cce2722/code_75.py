def max_points_to_earn(a):
    n = len(a)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if a[i - 1] == a[0]:
            dp[i] = dp[i - 1]
        else:
            dp[i] = max(dp[i - 1], dp[i - 2]) if i > 1 else dp[i - 1]
    
    return dp[-1]

n = int(input())
a = list(map(int, input().split()))
print(max_points_to_earn(a))
