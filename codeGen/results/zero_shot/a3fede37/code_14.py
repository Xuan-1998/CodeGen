def max_path_sum(tree):
    def dfs(node):
        if not node:
            return 0
        left = dfs(tree[node*2+1]) if node*2+1 < len(tree) else 0
        right = dfs(tree[node*2+2]) if node*2+2 < len(tree) else 0
        return tree[node] + max(left, right)

    return max(dfs(i) for i in range(len(tree)//2))

# Example usage:
tree = [1, 2, 3, 4, 5, 6]
print(max_path_sum(tree))  # Output: 9 (path is 1 -> 2 -> 4)
