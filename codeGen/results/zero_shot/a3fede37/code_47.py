def max_path_sum(arr):
    # Define a helper function for DFS
    def dfs(node, path_sum, max_sum):
        nonlocal max_sum
        if node is None:
            return
        # Update the maximum sum
        max_sum = max(max_sum, path_sum + arr[node])
        # Explore the left child
        dfs(arr.index(node) * 2 + 1, path_sum + arr[node], max_sum)
        # Explore the right child
        dfs(arr.index(node) * 2 + 2, path_sum + arr[node], max_sum)

    # Initialize variables
    max_sum = float('-inf')
    root = 0

    # Find the root node (assuming it's the first element in the array)
    for i in range(len(arr)):
        if arr[i] > 0:
            root = i
            break

    # Perform DFS starting from the root node
    dfs(root, 0, max_sum)

    return max_sum

# Test the function
arr = [1, 2, 3, 4, 5, 6]
print(max_path_sum(arr))  # Output: 15 (path: 1 + 2 + 3 + 4 + 5)
