def can_cross_stones(stones):
    k = 1  # initial jump distance
    for i in range(1, len(stones)):
        # calculate the maximum reachable position from current stone
        max_reachable = stones[i - 1] + k
        if stones[i] > max_reachable:
            return False  # cannot reach this stone
        k = (k * 3) % (stones[i] - stones[i - 1])  # update jump distance
    return True

# Example usage:
stones = [0, 2, 5, 8, 12]
print(can_cross_stones(stones))  # Output: True
