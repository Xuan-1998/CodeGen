def can_reach_last_index(arr):
    max_reach = 0
    for i in range(len(arr)):
        farthest_reachable = min(i + arr[i], len(arr) - 1)
        if farthest_reachable >= len(arr) - 1:
            return True
        max_reach = max(max_reach, farthest_reachable)
    return False

# Example usage:
arr = [2, 3, 0, 1]
print(can_reach_last_index(arr))  # Output: True

arr = [2, 3, 4, 5]
print(can_reach_last_index(arr))  # Output: False
