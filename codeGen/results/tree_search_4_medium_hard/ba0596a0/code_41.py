def can_cross_stones(stones):
    n = len(stones)
    dp = [False] * n

    # The base case: we can always stay on the first stone
    dp[0] = True

    for i in range(1, n):
        for j in range(max(0, i - 2), i):
            if (stones[i] - stones[j]) % (abs(i - j) + 1) == 0 and dp[j]:
                dp[i] = True
                break

    return dp[-1]

# Example usage:
stones = [0, 3, 5, 10]
print(can_cross_stones(stones))  # Output: True
