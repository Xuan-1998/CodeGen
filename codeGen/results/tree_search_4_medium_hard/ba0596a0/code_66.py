def can_cross_stones(stones):
    n = len(stones)
    dp = [[False] * (n // 2) for _ in range(n)]
    
    # Base case: it's always possible to reach the first stone
    dp[0][0] = True
    
    for i in range(1, n):
        for k in range(min(i, stones[i - 1]), -1, -1):
            if dp[i - k - 1][max(k - 1, 0)]:
                dp[i][k] = True
    
    return dp[-1][-1]

# Example usage
stones = [0, 2, 5, 7]
print(can_cross_stones(stones))  # Output: True
