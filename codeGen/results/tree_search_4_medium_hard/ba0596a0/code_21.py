def can_cross_stones(stones):
    n = len(stones)
    dp = [0] * n

    # Base case: the frog can always reach the first stone
    dp[0] = 1

    for i in range(1, n):
        k = stones[i] - stones[i-1]
        if (k % 3 == 0 or k % 3 == 2) and dp[(i-k//3)-1] == 1:
            dp[i] = 1
        else:
            dp[i] = 0

    return dp[-1]

# Example usage:
stones = [0, 5, 10, 15, 20]
print(can_cross_stones(stones))  # Output: 1
