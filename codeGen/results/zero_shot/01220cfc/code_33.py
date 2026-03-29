def can_reach_last_index(arr):
    n = len(arr)
    max_reachable_idx = 0

    for i in range(n):
        if i + arr[i] >= n - 1:  # Can we reach the last index from here?
            return True
        max_reachable_idx = max(max_reachable_idx, i + arr[i])

    return False

# Example usage:
arr = [2, 3, 1, 1, 4]
print(can_reach_last_index(arr))  # Output: True
