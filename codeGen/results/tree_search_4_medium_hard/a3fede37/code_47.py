def maxPathSum(tree):
    n = len(tree)
    dp = [0] * n

    # Base case: root node
    if tree[0] >= 0:
        dp[0] = tree[0]
    else:
        return float('-inf')

    for i in range(1, n):
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        # If both children exist, take the maximum of their sums and add the current node's value
        if left_child < n and right_child < n:
            dp[i] = max(dp[left_child], dp[right_child]) + tree[i]
        # If only the left child exists, take its sum and add the current node's value
        elif left_child < n:
            dp[i] = dp[left_child] + tree[i]
        # If only the right child exists, take its sum and add the current node's value
        elif right_child < n:
            dp[i] = dp[right_child] + tree[i]
        # Otherwise, just consider the current node's value
        else:
            dp[i] = tree[i]

    return max(dp)
