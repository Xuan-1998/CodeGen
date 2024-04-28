def is_divisible(sum):
    return sum % m == 0

def solve(n, m, arr):
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(m + 1):
            if arr[i - 1] <= j:
                dp[i][j] = or(dp[i - 1][j], is_divisible(arr[i - 1]) and dp[i - 1][j - arr[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]
    
    return int(any(dp[n]))
