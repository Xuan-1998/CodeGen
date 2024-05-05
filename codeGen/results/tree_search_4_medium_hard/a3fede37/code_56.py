def max_path_sum(tree):
    def dp(i, memo={}):
        if i in memo:
            return memo[i]
        if tree[i-1] == -1:  # leaf node
            return tree[i-1]
        left_child = (i * 2) + 1
        right_child = (i * 2) + 2
        max_sum = max(tree[i-1], dp(left_child, memo) + tree[i-1], dp(right_child, memo) + tree[i-1])
        memo[i] = max_sum
        return max_sum

    n = len(tree)
    root_node = (n - 1) // 2
    return dp(root_node)
