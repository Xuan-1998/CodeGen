def can_reach_end(arr):
    curr_idx = 0
    max_reachable_idx = 0

    for i in range(len(arr)):
        jump_len = arr[i]
        max_reachable_idx = max(max_reachable_idx, i + jump_len)
        if max_reachable_idx >= len(arr) - 1:
            return True
    return False

# Example usage
arr = [2, 3, 1, 1, 4]
print(can_reach_end(arr))  # Output: True
