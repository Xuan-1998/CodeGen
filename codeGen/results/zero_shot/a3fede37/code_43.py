def max_path_sum(tree):
    def dfs(node, current_sum):
        if node is None:
            return 0

        left_sum = dfs(tree[node*2-1], current_sum + tree[node])
        right_sum = dfs(tree[node*2], current_sum + tree[node])

        return max(left_sum, right_sum) + tree[node]

    max_sum = float('-inf')
    for i in range(len(tree)//2):
        max_sum = max(max_sum, dfs(i+1, tree[i]))

    return max_sum
