class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_path_sum(root):
    if root is None:
        return 0
    
    left_sum = max(0, max_path_sum(root.left))
    right_sum = max(0, max_path_sum(root.right))
    
    root_val = root.val
    path_sum = root_val + left_sum + right_sum
    
    return max(path_sum, root_val)
