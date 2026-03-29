def can_cross(stones):
    prev_jump = -1
    for i in range(1, len(stones)):
        curr_jump = stones[i] - stones[i-1]
        if abs(curr_jump - prev_jump) > 2:
            return False
        prev_jump = curr_jump
    return True

# Example usage
stones = [0, 3, 5, 7, 9, 12]
print(can_cross(stones))  # Output: True
