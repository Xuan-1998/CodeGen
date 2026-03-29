import sys

def max_path_sum(tree):
    n = len(tree)
    dp = [[0, -float('inf'), -float('inf')] for _ in range(n)]

    # Base case: leaf nodes have no children
    for i in range(1, n):
        if tree[i] == 0:
            dp[i][0] = tree[i-1]
            dp[i][1] = -float('inf')
            dp[i][2] = -float('inf')
        else:
            # Calculate the maximum sum of the left child
            max_left_sum = max(dp[j][0] + tree[j-1] for j in range(1, i))
            dp[i][1] = max_left_sum

            # Calculate the maximum sum of the right child
            max_right_sum = max(dp[k][0] + tree[k-1] for k in range(i+1, n))
            dp[i][2] = max_right_sum

            # The maximum sum of a path ending at node i is the maximum of its left child's maximum sum and its right child's maximum sum plus the value of node i
            dp[i][0] = max(dp[i][1], dp[i][2]) + tree[i-1]

    return dp[0][0]
