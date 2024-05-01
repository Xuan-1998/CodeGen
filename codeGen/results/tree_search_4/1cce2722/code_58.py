def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        if a[i-1] == a[0]:
            dp[i][0] = dp[i-1][0]
        elif a[i-1] > a[0]:
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
        else:
            dp[i][0] = max(dp[i-1][0], dp[i-1][-2])
    
    return dp[n][0]
