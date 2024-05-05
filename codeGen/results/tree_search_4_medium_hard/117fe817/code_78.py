def findCount(n):
    MOD = 10**9 + 7
    dp = [[0] * (n + 1) for _ in range(11)]
    
    # Base case: no integers, so count is 0 for all j
    for j in range(n + 1):
        dp[0][j] = 0
    
    for i in range(1, n + 1):
        for j in range(min(i, 9) + 1):
            if j == 0:
                # Count numbers less than or equal to i that start with '1'
                dp[i][j] = (i // 10 + 1) * (n - i)
            else:
                # Add count of integers with j-1 '1's and recursively call dp
                k = max(0, (i - 1) // 10)
                dp[i][j] = (dp[k][j - 1] + n - (k * 10 + 9)) % MOD
    
    # Calculate total count by summing up all dp values
    return sum(dp[i][j] for i in range(11) for j in range(n + 1))

n = int(input())
print(findCount(n))
