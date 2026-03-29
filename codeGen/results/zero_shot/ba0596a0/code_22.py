def can_frog_cross(stone_positions):
    if len(stone_positions) < 2:
        return True

    max_jump_distance = stone_positions[1] - stone_positions[0]

    for i in range(1, len(stone_positions)):
        if stone_positions[i] - stone_positions[i-1] > max_jump_distance + 1:
            return False

    return True

stone_positions = [int(x) for x in input().split()]
print(can_frog_cross(stone_positions))
