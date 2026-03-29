def find_max_sum_path(tree):
    # Step 1: Create a dictionary to represent the binary tree
    # This dictionary will map each node to its left and right children
    node_to_children = {}
    for i in range(0, len(tree), 2):
        node_id = tree[i]
        if i + 1 < len(tree):
            left_child = tree[i+1]
        else:
            left_child = None
        if i + 2 < len(tree):
            right_child = tree[i+2]
        else:
            right_child = None
        node_to_children[node_id] = (left_child, right_child)
    
    # Step 2: Create a dictionary to store the maximum sum of paths ending at each node
    max_sum_ending_at_node = {node: float('-inf') for node in node_to_children}
    max_sum_ending_at_node[tree[0]] = tree[0]
    
    # Step 3: Iterate through the nodes and update the maximum sum of paths ending at each node
    for node_id, (left_child, right_child) in node_to_children.items():
        if left_child is not None:
            max_sum_ending_at_node[node_id] = max(max_sum_ending_at_node.get(left_child, 0), tree[2*i+1])
        if right_child is not None:
            max_sum_ending_at_node[node_id] = max(max_sum_ending_at_node.get(node_id, 0), tree[2*i+2])
    
    # Step 4: Return the maximum sum of paths in the binary tree
    return max(max_sum_ending_at_node.values())
