import sys

def min_operations(root):
    # Initialize the result
    res = 0
    
    # Traverse the tree recursively
    def traverse(node):
        nonlocal res
        
        # If this is not the root, we need to adjust the value
        if node != root:
            res += 1
        
        # Recursively traverse the children
        for child in children[node]:
            traverse(child)
    
    # Traverse the tree starting from the root
    traverse(root)
    
    return res

# Read input and calculate the result
n = int(sys.stdin.readline())
parents = [int(x) for x in sys.stdin.readline().split()]
ranges = [[int(x), int(y)] for _ in range(n-1)]
root = 1  # Assuming the root is vertex 1

res = min_operations(root)

# Print the result
print(res)
