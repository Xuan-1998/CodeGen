def can_cross(stones):
    n = len(stones)
    dp = [True]  # Base case: frog can reach first stone

    for i in range(1, n):
        k = stones[i] - stones[i-1]
        for j in range(i):
            if abs(stones[i] - stones[j]) - abs(stones[i-1] - stones[j]) <= k:
                dp.append(dp[-1] or dp[j])
                break
        else:
            dp.append(True)

    return dp[-1]

# Example usage:
stones = [0, 2, 5, 7, 10]
print(can_cross(stones))  # Output: True

