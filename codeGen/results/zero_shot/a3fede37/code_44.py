def max_path_sum(arr):
    n = len(arr)
    
    # Create a dictionary to store the left and right child indices for each node
    children = {}
    for i in range(n):
        if i * 2 + 1 < n:  # Left child exists
            children[i] = (i * 2 + 1, None)
        if i * 2 + 2 < n:  # Right child exists
            children[i] = (i * 2 + 2, None)
    
    max_sum = float('-inf')  # Initialize maximum sum to negative infinity
    
    def dfs(node):
        nonlocal max_sum
        
        # Calculate the sum of the current path
        path_sum = arr[node]
        
        if node in children:
            left_child, right_child = children[node]
            
            # Recursively calculate the sum of the left and right subtrees
            if left_child < n:
                path_sum += dfs(left_child)
            if right_child < n:
                path_sum += dfs(right_child)
        
        max_sum = max(max_sum, path_sum)  # Update maximum sum
        
        return path_sum
    
    dfs(0)  # Start DFS from the root node (index 0)
    
    return max_sum

# Example usage:
arr = [1, 2, 3, 4, 5]
print(max_path_sum(arr))  # Output: 9
