def min_operations(n):
    # Initialize segment tree with initial ranges for each node
    seg_tree = [[10**9, 1] for _ in range(n)]

    def dfs(node, parent):
        if node != 0:  # Root node has no parent
            left_child_range = [max(0, r[0]-seg_tree[parent][0]), min(r[1], r[1]-seg_tree[parent][1])]
            right_child_range = [max(0, r[0]-seg_tree[parent][0]), min(r[1], r[1]-seg_tree[parent][1])]

            # Update segment tree for left child
            seg_tree[node] = [min(left_child_range[0], seg_tree[parent][0]), max(left_child_range[1], seg_tree[parent][1])]
            dfs(2*node+1, node)  # Recurse on left child

            # Update segment tree for right child
            if 2*node+2 < n:  # Check if right child exists
                seg_tree[node] = [min(right_child_range[0], seg_tree[parent][0]), max(right_child_range[1], seg_tree[parent][1])]
                dfs(2*node+2, node)  # Recurse on right child

            # Calculate difference between current node's range value and min/max range values in subtree
            diff = (r[0]-seg_tree[node][0]) if r[0] > seg_tree[node][0] else 0
            diff += (seg_tree[node][1]-r[1]) if seg_tree[node][1] < r[1] else 0

            # Update total number of operations needed
            return max(0, diff)

    # Start DFS traversal from root node
    return dfs(0, -1)
