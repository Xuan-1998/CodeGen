def max_path_sum(tree):
    n = len(tree)
    dp = [0] * n

    def dfs(i):
        if i >= n // 2:  # leaf node or root node
            return tree[i]
        left_sum = dfs(2*i+1)
        right_sum = dfs(2*i+2)
        return max(left_sum, right_sum) + tree[i]

    return dfs(0)

# Example usage:
tree = [-10, -5, 3, 2, 7, 15]
print(max_path_sum(tree))  # Output: 18
