def max_path_sum(arr):
    # Step 1: Define a helper function to find the maximum sum of a path starting at each node
    def dfs(node, parent=None):
        if node is None:
            return 0
        
        left_sum = right_sum = 0
        
        # Step 2: Recursively calculate the maximum sum of paths for the left and right subtrees
        if 2*node + 1 < len(arr):  # Check if left child exists
            left_sum = dfs(2*node + 1, node)
        
        if 2*node + 2 < len(arr):  # Check if right child exists
            right_sum = dfs(2*node + 2, node)
        
        # Step 3: Calculate the maximum sum of a path starting at this node
        max_sum = arr[node]  # The value of the current node
        if parent is not None:
            max_sum += min(left_sum, right_sum)  # Add the minimum sum of the left and right subtrees
        
        return max_sum
    
    # Step 4: Find the maximum sum of a path starting at any node in the tree
    max_path = dfs(0)
    
    print(max_path)

# Example usage:
arr = [1, -2, 3, 10, -4, 8, 3]
max_path_sum(arr)
