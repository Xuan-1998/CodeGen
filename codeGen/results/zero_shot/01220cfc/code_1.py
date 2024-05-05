def can_reach_last_index(arr):
    n = len(arr)
    i = 0
    for j in range(n - 1):
        if i + arr[j] < j + 1:  # Can't reach the next index
            return False
        i = max(i, j)  # Update our current position
    return True

# Example usage:
arr = [2, 3, 0, 4]
print(can_reach_last_index(arr))  # Output: True

arr = [1, 1, 1, 1]
print(can_reach_last_index(arr))  # Output: False
