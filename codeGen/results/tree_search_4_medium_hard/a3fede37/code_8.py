def max_path_sum(tree):
    memo = {}

    def helper(node):
        if node is None:
            return 0

        if node in memo:
            return memo[node]

        left_sum = helper(tree[2 * node])
        right_sum = helper(tree[2 * node + 1])

        if tree[node] > left_sum and tree[node] > right_sum:
            memo[node] = tree[node]
        elif left_sum + tree[node] > right_sum + tree[node]:
            memo[node] = left_sum + tree[node]
        else:
            memo[node] = right_sum + tree[node]

        return memo[node]

    root = 0
    for i in range(len(tree) // 2):
        if tree[i] != -1:
            root = i

    print(helper(root))
