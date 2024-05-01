from collections import defaultdict

def has_subset_sum(arr, m):
    n = len(arr)
    
    # Base cases
    if n == 0 and m != 0:
        return 1 if m == 0 else 0
    if m == 0:
        return 1
    
    dp = defaultdict(int)
    dp[0][0] = 1
    
    for i in range(1, n+1):
        for j in range(m+1):
            dp[i][j] = dp[i-1][j]
            if j >= arr[i-1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-arr[i-1]] + 1)
    
    return dp[n][m]

n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(has_subset_sum(arr, m))
