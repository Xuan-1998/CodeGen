def max_sum_of_path(root):
    def calculate_max_sum(node):
        if node is None:
            return 0

        left_sum = calculate_max_sum(tree[node*2+1]) if node * 2 + 1 < len(tree) else 0
        right_sum = calculate_max_sum(tree[node*2+2]) if node * 2 + 2 < len(tree) else 0

        return max(node, node + left_sum, node + right_sum)

    tree = [int(x) for x in input().split()]
    root_index = (len(tree) - 1) // 2
    return calculate_max_sum(root_index)
