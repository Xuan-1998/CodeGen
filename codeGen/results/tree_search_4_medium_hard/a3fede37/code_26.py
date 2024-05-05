def maxPathSum(root):
    def dfs(node):
        if node is None:
            return 0
        
        left_sum = max(0, dfs(node.left))
        right_sum = max(0, dfs(node.right))

        price_newpath = node.val + left_sum + right_sum

        nonlocal max_sum
        max_sum = max(max_sum, price_newpath)

        return node.val + max(left_sum, right_sum)

    max_sum = float('-inf')
    dfs(root)
    return max_sum
