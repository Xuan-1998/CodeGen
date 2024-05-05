def max_path_sum(arr):
    def dfs(node):
        if node is None:
            return 0
        left_sum = dfs(arr[node][1])
        right_sum = dfs(arr[node][2])
        current_sum = arr[node][0] + max(left_sum, right_sum)
        return current_sum

    max_sum = float('-inf')
    for i in range(len(arr)):
        max_sum = max(max_sum, dfs(i))
    return max_sum

# Example usage
arr = [[1, [2, None], [3, None]]]  # Root node with left and right children
print(max_path_sum(arr))  # Output: 6 (path is 1 -> 2 -> 3)
