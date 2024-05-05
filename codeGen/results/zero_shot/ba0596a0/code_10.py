def can_cross_stones(stone_positions):
    def dfs(index, jump_distance):
        if index == len(stone_positions) - 1:
            return True
        for k in range(3):
            new_jump_distance = jump_distance + (k - 1)
            if stone_positions[index + 1] - stone_positions[index] == new_jump_distance:
                if dfs(index + 1, new_jump_distance):
                    return True
        return False

    return dfs(0, 0)

stone_positions = [int(x) for x in input().split()]
print(can_cross_stones(stone_positions))
