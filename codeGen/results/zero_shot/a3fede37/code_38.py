class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def parse_tree(arr):
    if not arr:
        return None
    
    root = TreeNode(arr[0])
    stack = [(root, 1)]
    
    for i in range(1, len(arr)):
        node, index = stack.pop()
        
        if arr[i] is not None:
            if index * 2 + 1 <= len(arr):
                node.left = TreeNode(arr[index * 2 + 1])
                stack.append((node.left, index * 2 + 1))
            if index * 2 + 2 <= len(arr):
                node.right = TreeNode(arr[index * 2 + 2])
                stack.append((node.right, index * 2 + 2))
    
    return root

def max_path_sum(root):
    max_sum = float('-inf')
    
    def dfs(node):
        nonlocal max_sum
        
        if node is None:
            return 0
        
        left_sum = dfs(node.left)
        right_sum = dfs(node.right)
        
        current_sum = node.value + left_sum + right_sum
        
        max_sum = max(max_sum, current_sum)
        
        return node.value + max(left_sum, right_sum) + node.value
    
    dfs(root)
    
    return max_sum

# Example usage:
arr = [1, 2, 3, None, 4, 5, None, 6]
root = parse_tree(arr)
print(max_path_sum(root))  # Output: 15
