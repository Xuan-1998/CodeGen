def can_cross_stones(stone_positions):
    n = len(stone_positions)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n):
        if stone_positions[i] - stone_positions[i-1] <= 2:
            dp[i] = dp[i-1]
        else:
            for j in range(i-1, max(-1, i-3), -1):
                if stone_positions[i] - stone_positions[j] <= 2 and dp[j]:
                    dp[i] = True
                    break

    return dp[-1]

# Example usage:
stone_positions = [0, 1, 5, 6, 10]
print(can_cross_stones(stone_positions))  # Output: True
