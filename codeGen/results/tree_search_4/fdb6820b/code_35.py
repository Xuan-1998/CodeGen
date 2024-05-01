def count_ways_to_form_sum(m, N):
    dp = [[0] * (N + 1) for _ in range(m + 1)]
    
    # Base cases
    for i in range(1, m + 1):
        dp[i][0] = sum(range(i))
    dp[0][0] = 1
    
    # Recursive case
    for i in range(1, m + 1):
        for j in range(min(i, N) + 1):
            if j < i:
                dp[i][j] = dp[i-1][j]
            elif j >= i:
                dp[i][j] = sum(dp[k][j-k] for k in range(1, i)) + (dp[i-1][0] if i > 1 else 0)
    
    # Return the total number of ways to form a sum of N
    return dp[m][N] % (10 ** 9 + 7)

# Example usage:
m, N = map(int, input().split())
print(count_ways_to_form_sum(m, N))
