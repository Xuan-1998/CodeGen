# Step 1: Define the function to solve the problem
def max_path_sum(arr):
    # Step 2: Calculate the number of nodes in the tree
    n = len(arr)
    
    # Step 3: Create a dictionary to represent the binary tree
    tree = {}
    for i in range(n // 2):
        parent = (i * 2) if i % 2 == 0 else ((i * 2) + 1)
        child = (n - 1) - i
        tree[parent] = [child, arr[child]]
    
    # Step 4: Define a function to calculate the maximum path sum of a subtree rooted at a node
    def max_path_sum_node(node):
        if node not in tree:
            return 0
        
        left_child = tree[node][0]
        right_child = tree[node][1]
        
        # Calculate the maximum path sum of the current node and its children
        max_sum = arr[node] + max(0, max_path_sum_node(left_child)) + max(0, max_path_sum_node(right_child))
        
        return max_sum
    
    # Step 5: Find the root of the tree (the first element in the array)
    root = 0
    
    # Step 6: Calculate and return the maximum path sum
    return max_path_sum_node(root)

# Step 7: Read input from stdin, call the function, and print the output to stdout
arr = [int(x) for x in input().split()]
print(max_path_sum(arr))
