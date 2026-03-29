def max_path_sum(tree):
    n = len(tree) // 4  # Number of nodes in the tree
    max_sum = float('-inf')

    def dfs(node):
        nonlocal max_sum
        if node >= len(tree):  # Base case: reached a leaf node
            return

        left_sum = tree[node]
        right_sum = tree[node + 1]

        if left_sum > 0 and right_sum > 0:
            # Recursively explore the left and right subtrees
            left_max_sum = dfs(2*node + 1)
            right_max_sum = dfs(2*node + 2)

            # Update the maximum sum of the current path
            max_sum = max(max_sum, left_sum + left_max_sum, right_sum + right_max_sum)
        else:
            # No children, so the maximum sum is just the value of this node
            max_sum = max(max_sum, tree[node])

    for i in range(n):  # Start DFS from each node
        dfs(i)

    return max_sum

tree = read_tree()
print(max_path_sum(tree))
