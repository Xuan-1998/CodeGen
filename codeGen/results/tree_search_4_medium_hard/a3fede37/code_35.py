class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_path_sum(arr):
    n = len(arr) // 2
    root = Node(arr[0])
    stack = [(root, i)]
    
    for _ in range(n - 1):
        node, i = stack.pop()
        if arr[i * 2 + 1] != 0:
            node.left = Node(arr[i * 2 + 1])
            stack.append((node.left, i * 2 + 1))
        if arr[i * 2 + 2] != 0:
            node.right = Node(arr[i * 2 + 2])
            stack.append((node.right, i * 2 + 2))
    
    def max_path_sum_node(node):
        nonlocal max_sum
        if not node:
            return 0
        
        left_sum = max_path_sum_node(node.left)
        right_sum = max_path_sum_node(node.right)
        
        max_sum = max(max_sum, node.val + left_sum + right_sum)
        return node.val + max(left_sum, right_sum)
    
    max_sum = float('-inf')
    max_path_sum_node(root)
    return max_sum

# Read input from stdin
arr = [int(x) for x in input().split()]

print(max_path_sum(arr))
