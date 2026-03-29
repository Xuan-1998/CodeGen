def construct_tree(tree):
    def dfs(node):
        if node >= len(tree):
            return None
        left = dfs(2*node+1)
        right = dfs(2*node+2)
        return [tree[node], left, right]

    return dfs(0)
