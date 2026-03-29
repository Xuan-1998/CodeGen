def can_cross_stones(stones):
    if len(stones) < 3:
        return True

    for i in range(1, min(2, stones[1] - stones[0])):
        if stones[i + 1] - stones[i] > 2:
            return False

    def helper(stones, current_position):
        if current_position >= len(stones) - 1:
            return True
        for i in range(-1, 3):
            if current_position + i >= 0 and current_position + i < len(stones) - 1 and abs(stones[current_position + i] - stones[current_position]) == i:
                if helper(stones, current_position + i):
                    return True
        return False

    return helper(stones, 0)

stones = [int(x) for x in input().split()]
print(can_cross_stones(stones))
