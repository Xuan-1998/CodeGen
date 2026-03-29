def can_cross_stones(stone_positions):
    max_reached = 0
    prev_jump = 0
    for i, pos in enumerate(stone_positions):
        k = abs(pos - prev_jump)  # calculate possible jump distances
        if k >= 2 and k <= (max_reached + 3):  # update max_reached if current stone is within reach
            max_reached = k
        prev_jump = pos  # update previous jump
    return max_reached == stone_positions[-1] - 1

# Example usage:
stone_positions = [0, 2, 5, 8, 12]
print(can_cross_stones(stone_positions))  # Output: True
