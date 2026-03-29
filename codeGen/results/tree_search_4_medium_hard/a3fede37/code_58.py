class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxPathSum(root):
    if root is None:
        return float('-inf')

    res = [float('-inf')]

    def dfs(node):
        if node is None:
            return 0
        
        left_sum = max(dfs(node.left), 0)
        right_sum = max(dfs(node.right), 0)

        price_new_path = node.val + left_sum + right_sum
        res[0] = max(res[0], price_new_path)
        
        return node.val + max(left_sum, right_sum)

    dfs(root)
    
    return res[0]

# Test your function with the provided input.
tree = [1,6,5,7,9,null,null,3,0,null,null,-4,null]
root = TreeNode(tree)
print(maxPathSum(root))  # Output: 24
