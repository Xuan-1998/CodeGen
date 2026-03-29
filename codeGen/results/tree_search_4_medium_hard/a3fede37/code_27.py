def max_path_sum(root):
    def dfs(node):
        if not node:
            return 0

        left_sum = dfs(node[1])
        right_sum = dfs(node[2])

        current_sum = node[0]
        if left_sum > 0:
            current_sum += left_sum
        if right_sum > 0:
            current_sum += right_sum

        nonlocal max_sum
        max_sum = max(max_sum, current_sum)

        return current_sum

    root_val, *left_child, right_child = root
    max_sum = float('-inf')

    dfs(root)
    return max_sum
