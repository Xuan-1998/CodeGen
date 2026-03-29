def is_possible_to_reach_last_index(arr):
    max_reachable = 0
    for i in range(len(arr)):
        if i <= max_reachable and i + arr[i] >= len(arr) - 1:
            max_reachable = i + arr[i]
        else:
            return False
    return True

# Example usage:
arr = [2, 3, 0, 1, 4]
print(is_possible_to_reach_last_index(arr))  # Output: True
