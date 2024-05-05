def min_operations(n, parent, value_range):
    # Create a DP table to store the minimum number of operations
    dp = [[0] * (10**9 + 1) for _ in range(n + 1)]

    def dfs(node):
        # Base case: leaf node
        if not parent[node]:
            return sum((value - l) // (r - l) for value, (l, r) in enumerate(value_range))

        max_val = 0
        min_ops = float('inf')
        for child in range(1, n):
            if parent[child] == node:
                # Calculate the minimum number of operations for the child subtree
                ops = dfs(child)
                # Update the maximum value and minimum operations
                max_val = max(max_val, max(value_range[child][1], r))
                min_ops = min(min_ops, ops + (value_range[child][1] - l) // (r - l))

        dp[node][0] = 0
        for i in range(1, 10**9 + 1):
            if value_range[node][1] < i:
                break
            if max_val < i:
                dp[node][i] = min_ops
            else:
                dp[node][i] = dp[node][max_val - (i - l)] + (value_range[node][1] - i) // (r - i)

        return dp[node][max_val]

    # Perform DFS from the root node
    max_ops = 0
    for i in range(n):
        if parent[i]:
            max_ops = max(max_ops, dfs(i))

    print(max_ops)
