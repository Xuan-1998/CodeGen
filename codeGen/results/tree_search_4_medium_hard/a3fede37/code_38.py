===BEGIN CODE===
from collections import defaultdict

def max_sum_tree(tree):
    n = len(tree)
    dp = [0] * (n + 1)

    def dfs(node, left=True):
        if left:
            return tree[node][0], tree[node][1]
        else:
            return -tree[node][0], -tree[node][1]

    for node in range(1, n+1):
        left_max_sum, _ = dfs(tree[node-1][2] if node % 2 != 0 else 0, True)
        right_max_sum, _ = dfs(tree[node//2][2] if node % 2 == 0 else 0, False)

        dp[node] = max(node, left_max_sum + node, right_max_sum + node)

    return max(dp[1:])

===END CODE===
