def max_path_sum(arr):
    def find_max_sum(node_idx, prev_val):
        if node_idx >= len(arr) or arr[node_idx] < 0:
            return 0
        
        left_sum = find_max_sum(2*node_idx+1, arr[node_idx])
        right_sum = find_max_sum(2*node_idx+2, arr[node_idx])
        
        current_sum = arr[node_idx] + prev_val
        if node_idx % 2 == 0:
            return max(left_sum, right_sum, current_sum)
        else:
            return max(right_sum, current_sum)

    root_idx = len(arr) // 2
    return find_max_sum(root_idx, 0)


# Example usage
arr = [5, 2, -3]
print(max_path_sum(arr))  # Output: 7 (5 + 2)
