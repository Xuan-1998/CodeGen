def possible_to_delete(tree, memo):
    n = len(tree)
    res = [False] * (n + 1)

    def dfs(node):
        if res[node]:
            return res[node]
        res[node] = True

        for child in tree[node]:
            if not dfs(child):
                res[node] = False
                break

        return res[node]

    for node in range(1, n + 1):
        if not memo.get(node):
            dfs(node)

    return res[1]
