# Step 1: Understand the problem
The goal is to find the maximum sum of a path in a binary tree represented as an array.

# Step 2: Define a Node class (not necessary but helpful)
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Step 3: Convert the array to a binary tree
def arrayToTree(arr):
    if not arr:
        return None
    
    root = Node(arr[0])
    nodes = [root]
    i = 1
    while i < len(arr):
        node = Node(arr[i])
        nodes[-1].left = node
        nodes.append(node)
        i += 1
        if i >= len(arr): break
        node = Node(arr[i])
        nodes[-1].right = node
        nodes.append(node)
        i += 1
    return root

# Step 4: Calculate the maximum sum of a path in the binary tree
def maxPathSum(root):
    max_sum = float('-inf')

    def dfs(node, current_sum):
        nonlocal max_sum
        if not node:
            return
        
        current_sum += node.val
        
        left_sum = dfs(node.left, current_sum) if node.left else 0
        right_sum = dfs(node.right, current_sum) if node.right else 0
        
        max_sum = max(max_sum, current_sum)
        
        return max(current_sum, left_sum + right_sum)

    dfs(root, root.val)
    return max_sum

# Step 5: Read input from stdin and print the output to stdout
root = arrayToTree([int(x) for x in input().split()])
print(maxPathSum(root))
