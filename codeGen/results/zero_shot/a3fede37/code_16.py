def max_path_sum(tree):
    # Define a helper function to calculate the maximum sum of a path
    def max_path_sum_helper(index):
        # Calculate the value of the node at this index
        node_val = tree[index]
        
        # Recursively call ourselves on the left and right child indices
        left_sum = max_path_sum_helper(2 * index + 1) if 2 * index + 1 < len(tree) else 0
        right_sum = max_path_sum_helper(2 * index + 2) if 2 * index + 2 < len(tree) else 0
        
        # Calculate the maximum sum of a path from this node to any leaf node
        return node_val + max(left_sum, right_sum)
    
    # Start the recursion by calling ourselves on the root node (index 0)
    return max_path_sum_helper(0)

# Test the function
tree = [1, -2, 3, 10, -4, 7, 9]
print(max_path_sum(tree))  # Should print 18
