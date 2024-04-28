def find_subset_sum_divisible_by_m(n, m):
    dp = [[False] * (m + 1) for _ in range(sum(range(1, n+1)) + 1)]
    
    for i in range(1, sum(range(1, n+1)) + 1):
        if i < m:
            dp[i][0] = True
        else:
            dp[i][0] = (i % m == 0)
        
        for j in range(1, min(i, m) + 1):
            if i - j >= 0:
                dp[i][j] = dp[i-j][j-1] or dp[i-j][j]
    
    return 1 if any(dp[-1]) else 0

n = int(input())
m = int(input())
arr = list(map(int, input().split()))
print(find_subset_sum_divisible_by_m(n, m))
