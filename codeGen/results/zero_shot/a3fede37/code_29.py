def max_path_sum(arr):
    # Find the root node (first element in the array)
    root = arr[0]

    # Initialize the maximum sum to negative infinity
    max_sum = float('-inf')

    def dfs(node, current_sum):
        nonlocal max_sum

        # Update the maximum sum if necessary
        max_sum = max(max_sum, current_sum + node)

        # Recursively explore each child node
        for i in range(1, len(arr)):
            if arr[i] == node:
                dfs(arr[i], current_sum + node)
                break

    dfs(root, 0)

    return max_sum
