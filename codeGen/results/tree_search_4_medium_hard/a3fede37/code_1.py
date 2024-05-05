def max_path_sum_in_tree(tree):
    def dfs(node, parent_value=0, max_path_sum_including_node=float('-inf'), max_path_sum_excluding_node=float('-inf')):
        left_sum = 0 if node[1] is None else dfs(tree[node[1]], node[0], max(parent_value + node[0], max_path_sum_including_node), max_path_sum_excluding_node)
        right_sum = 0 if node[2] is None else dfs(tree[node[2]], node[0], max(parent_value + node[0], max_path_sum_including_node), left_sum)
        
        return max(max_path_sum_including_node, parent_value + node[0]), max(left_sum, right_sum)

    return dfs(tree[0])[1]
