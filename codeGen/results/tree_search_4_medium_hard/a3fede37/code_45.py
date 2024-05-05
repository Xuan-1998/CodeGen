import sys

def max_path_sum(tree):
    n = len(tree)
    dp = [0] * n
    dp[0] = tree[0]
    for i in range(1, n):
        if 2*i+1 < n:  # left child exists
            dp[i] = max(dp[2*i+1], tree[i])  # consider the maximum sum of a path ending at the left child
        else:
            dp[i] = tree[i]
        if 2*i+2 < n:  # right child exists
            dp[i] += max(dp[2*i+2], 0)  # add the maximum sum of a path ending at the right child (or 0 if it doesn't exist)
    return max(dp)

# Read input from stdin
n = int(input())
tree = [int(x) for x in input().split()]

# Calculate and print the answer
print(max_path_sum(tree))
