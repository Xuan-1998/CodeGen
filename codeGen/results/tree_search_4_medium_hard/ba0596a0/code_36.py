def can_cross(stones):
    n = len(stones)
    dp = [False] * n
    dp[0] = True

    for i in range(1, n):
        for j in range(max(0, i - 2), min(i + 3, n)):
            if abs(j - i) in (1, 2) and dp[j]:
                dp[i] = True
                break

    return dp[-1]

# Example usage:
stones = [0, 1, 3, 5, 6, 8, 12, 17]
print(can_cross(stones))  # Output: True
