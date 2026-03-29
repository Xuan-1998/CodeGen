def can_cross_river(stones):
    memo = {}
    dp = [(0, 0, len(stones) - 1)]

    for i in range(1, len(stones)):
        k = (stones[i]-stones[i-1]) % 3
        if k == 0:
            k = 1

        for j in range(i):
            prev_frog_position, prev_jump_length, remaining_stones = dp[j]
            if prev_jump_length == k - 1 or prev_jump_length == k or prev_jump_length == k + 1:
                dp.append((i, k, remaining_stones - 1))
                break
        else:
            dp.append((i, k, remaining_stones))

    return dp[-1][0] == len(stones) - 1

# Example usage:
stones = [0, 3, 5, 6, 9]
print(can_cross_river(stones))  # Output: True
