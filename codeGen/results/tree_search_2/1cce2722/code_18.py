def max_points(a):
    n = len(a)
    dp = [[0] * 2 for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = dp[i - 1][1]
        
        if i >= 2:
            diff = a[i - 1] - a[i - 2]
            if i >= 3 and a[i - 1] - a[i - 2] == a[i - 3] - a[i - 4]:
                dp[i][0] += dp[i - 2][0] + diff
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 2][0])
                
            if i >= 3 and a[i - 1] - a[i - 2] == a[i - 4] - a[i - 5]:
                dp[i][1] += dp[i - 3][1] + diff
            else:
                dp[i][1] = max(dp[i - 1][1], dp[i - 3][1])
                
    return max(dp[n])

n = int(input())
a = list(map(int, input().split()))
print(max_points(a))
