def max_path_sum(tree):
    def is_valid_node_index(i):
        return 0 <= i < len(tree)

    def max_path_sum_from_node(node_idx):
        if not is_valid_node_index(node_idx):
            return 0
        
        left_child = 2 * node_idx + 1
        right_child = 2 * node_idx + 2

        max_left_sum = max_path_sum_from_node(left_child) if is_valid_node_index(left_child) else 0
        max_right_sum = max_path_sum_from_node(right_child) if is_valid_node_index(right_child) else 0
        
        return tree[node_idx] + max(max_left_sum, max_right_sum)

    max_sum = max_path_sum_from_node(0)
    
    print(max_sum)

# Example usage:
tree = [1, -2, 3, 10, -4, 6, 2]
max_path_sum(tree)
