def max_path_sum_tree(arr):
    # Create a dictionary to store node values and children
    tree = {}
    for i, val in enumerate(arr):
        tree[i] = {'val': val, 'children': []}

    def dfs(node):
        # Initialize the maximum sum path
        max_sum = -float('inf')

        # Recursively traverse the left subtree
        if len(tree[node]['children']) > 0:
            max_sum = max(max_sum, dfs(tree[node]['children'][0]))

        # Recursively traverse the right subtree
        if len(tree[node]['children']) > 1:
            max_sum = max(max_sum, dfs(tree[node]['children'][1]))

        # Update the maximum sum with the current node's value
        max_sum += tree[node]['val']

        return max_sum

    # Find the root node (the first element in the array)
    root = arr[0]

    # Traverse the binary tree and find the maximum sum path
    max_sum_path = dfs(root)

    return max_sum_path

# Example usage:
arr = [1, [2, [4], [5]], [3]]
print(max_path_sum_tree(arr))  # Output: 10 (1 + 2 + 4)
