def equal_to_zero():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [[0] * (sum(a) + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, sum(a) + 1):
            if j >= a[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-a[i-1]] + 1)
            else:
                dp[i][j] = dp[i-1][j]
    
    return "YES" if dp[n][-1] == 0 else "NO"

print(equal_to_zero())
