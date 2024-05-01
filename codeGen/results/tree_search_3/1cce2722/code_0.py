def max_points(n, seq):
    dp = [[0] * (107) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for k in range(1, 107):
            dp[i][k] = dp[i-1][k]
            
            if i > 0 and k == seq[i]:
                if i > 0 and (k - 1) in seq:
                    dp[i][k] = max(dp[i][k], dp[i-1][k-1] + 1)
                if i < n and (k+1) in seq:
                    dp[i][k] = max(dp[i][k], dp[i-1][k+1] + 1)

    return dp[n][106]

n = int(input())
seq = list(map(int, input().split()))
print(max_points(n, seq))
