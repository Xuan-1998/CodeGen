def max_path_sum(arr):
    # Parse the input array into a binary tree structure
    def build_tree(arr, start, end):
        if start > end:
            return None
        root = arr[start]
        left = build_tree(arr, 2*start+1, 2*end)
        right = build_tree(arr, 2*start+2, 2*end+1)
        return [root, left, right]

    tree = build_tree(arr, 0, len(arr)-1)

    # Define a function to calculate the maximum sum of a path in the tree
    def max_path_sum_helper(node):
        if node is None:
            return 0
        return node + max(max_path_sum_helper(2*node+1), max_path_sum_helper(2*node+2))

    # Traverse the tree and use the function to find the maximum sum
    max_sum = float('-inf')
    def traverse(node):
        nonlocal max_sum
        if node is None:
            return
        left_sum = max_path_sum_helper(2*node+1)
        right_sum = max_path_sum_helper(2*node+2)
        current_sum = node + left_sum + right_sum
        max_sum = max(max_sum, current_sum)
        traverse(2*node+1)
        traverse(2*node+2)

    # Start traversing the tree from the root
    traverse(tree[0])

    return max_sum

# Read input from stdin
arr = [int(x) for x in input().split()]

# Call the function and print the result to stdout
print(max_path_sum(arr))
