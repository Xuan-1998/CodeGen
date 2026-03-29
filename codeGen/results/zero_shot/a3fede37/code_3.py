class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def reconstruct_tree(arr):
    if not arr:
        return None
    
    root = Node(arr[0])
    stack = [(root, 0)]
    
    for i in range(1, len(arr)):
        node, j = stack.pop()
        
        if i < 2 * j + 1:
            node.left = Node(arr[i])
            stack.append((node.left, i))
        else:
            node.right = Node(arr[i])
            stack.append((node.right, i))
    
    return root

def max_sum_path(root):
    max_sum = float('-inf')
    stack = [(root, root.value)]
    
    while stack:
        node, sum_val = stack.pop()
        
        if node.left:
            stack.append((node.left, sum_val + node.left.value))
        
        if node.right:
            stack.append((node.right, sum_val + node.right.value))
        
        max_sum = max(max_sum, sum_val)
    
    return max_sum

def main():
    arr = [int(x) for x in input().split()]
    root = reconstruct_tree(arr)
    print(max_sum_path(root))

if __name__ == "__main__":
    main()
