def can_cross_river(stones):
    n = len(stones)
    dp = [False] * (n + 1)

    dp[0] = True

    for i in range(1, n + 1):
        for k in range(abs(i - 1), abs(i - stones[-1]), 2):
            j = max(0, i - k)
            if dp[j]:
                dp[i] = True
                break

    return dp[n]

# Example usage:
stones = [0, 3, 5, 10]
print(can_cross_river(stones))  # Output: True

stones = [0, 1, 4, 7]
print(can_cross_river(stones))  # Output: False
