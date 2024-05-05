def maxSumPath(root):
    def dfs(node):
        if not node:
            return 0
        left_sum = dfs(left_child)
        right_sum = dfs(right_child)
        return node + max(left_sum, right_sum)

    memo = {}
    def dfs_with_memo(node):
        if node in memo:
            return memo[node]
        left_sum = dfs_with_memo(left_child) if left_child else 0
        right_sum = dfs_with_memo(right_child) if right_child else 0
        memo[node] = node + max(left_sum, right_sum)
        return memo[node]

    root_value = int(input())
    left_child = int(input()) if input() != 'null' else None
    right_child = int(input()) if input() != 'null' else None

    max_sum = dfs_with_memo(root_value)

    print(max_sum)
