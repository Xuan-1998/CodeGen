def max_points(a):
    n = len(a)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if a[i - 1] % 2 == 1:
            dp[i] = max(dp[i-1], dp[i-2] + 1) if i >= 2 else 0
        else:
            dp[i] = max(dp[i-1], dp[i-2] - 1) if i >= 2 else 0
    
    return dp[-1]

n = int(input())
a = list(map(int, input().split()))
print(max_points(a))
