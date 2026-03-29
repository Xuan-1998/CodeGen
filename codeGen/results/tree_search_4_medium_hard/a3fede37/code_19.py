def maxPathSum(root):
    def helper(node):
        if not node:
            return 0

        # Calculate the maximum sum of the left subtree.
        left_sum = max(helper(node.left), 0)

        # Calculate the maximum sum of the right subtree.
        right_sum = max(helper(node.right), 0)

        # The maximum sum of the current path is the maximum of three options:
        #   1. Include the current node's value in the path.
        #   2. Exclude the current node's value, but consider the left subtree and rightSum[] for nodes in that subtree.
        #   3. Exclude the current node's value, but consider the right subtree and leftSum[] for nodes in that subtree.
        max_sum = node.val + max(left_sum, right_sum)

        # Update the maximum sum of the left and right subtrees.
        left_sum = max(left_sum, helper(node.left))
        right_sum = max(right_sum, helper(node.right))

        return max_sum

    root_val = root[0]
    for i in range(1, len(root)):
        if root[i] < 0:
            root[i - 1] += root[i]

    return helper([root_val])
