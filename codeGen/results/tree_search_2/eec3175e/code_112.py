def subset_sum_divisible_by_m(n, m, arr):
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    
    # Base case: sum of an empty set is always divisible by m
    for j in range(m + 1):
        dp[0][j] = True
    
    for i in range(1, n + 1):
        for j in range(m + 1):
            if j < arr[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = (dp[i - 1][j] or dp[i - 1][j - arr[i - 1]])
    
    # Check for the subset sum divisible by m
    for j in range(m // 2, m + 1):
        if dp[n][j]:
            return 1
    
    return 0

# Read input from stdin
n = int(input())
m = int(input())
arr = [int(x) for x in input().split()]

print(subset_sum_divisible_by_m(n, m, arr))
