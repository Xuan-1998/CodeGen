def maxPathSum(root):
    memo = {}

    def dfs(node):
        if node not in memo:
            left_sum = right_sum = 0
            if node * 2 + 1 < len(tree) and tree[node * 2 + 1] > 0:
                left_sum = dfs(node * 2 + 1)
            if node * 2 + 2 < len(tree) and tree[node * 2 + 2] > 0:
                right_sum = dfs(node * 2 + 2)

            memo[node] = tree[node] + max(left_sum, right_sum)
            return memo[node]
        return memo[node]

    tree = list(map(int, input().split()))
    root_index = tree.index(max(tree))
    return dfs(root_index)
