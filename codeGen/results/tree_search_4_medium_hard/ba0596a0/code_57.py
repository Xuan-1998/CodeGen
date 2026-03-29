def can_cross_stones(stones):
    n = len(stones)
    dp = [[False] * (n - 1) for _ in range(n)]

    # Base case: the frog can always reach stone 0
    for j in range(n - 1):
        dp[0][j] = True

    for i in range(1, n):
        for j in range(max(0, stones[i] - 2), min(n - 1, stones[i] + 2)):
            if dp[i-1][j-1] or dp[i-1][j] or dp[i-1][j+1]:
                dp[i][j] = True

    return any(dp[-1])

# Example usage:
stones = [0, 4, 9, 16, 25]
print(can_cross_stones(stones))  # Output: True
