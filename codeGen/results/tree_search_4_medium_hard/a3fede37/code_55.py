def maxPathSum(tree):
    # Initialize memoization dictionary
    memo = {}

    def dfs(i):
        if i in memo:
            return memo[i]

        # Base case: node has no children, maximum sum is the value of the node itself
        if not tree[2*i+1] and not tree[2*i+2]:
            return tree[i]

        # Calculate maximum sum considering left child
        left_sum = dfs(2*i+1) if 2*i+1 < len(tree) else -float('inf')

        # Calculate maximum sum considering right child
        right_sum = dfs(2*i+2) if 2*i+2 < len(tree) else -float('inf')

        # Maximum sum is the maximum of left and right sums plus the value of the current node
        memo[i] = max(left_sum, right_sum) + tree[i]
        return memo[i]

    # Start DFS from root (index 0)
    return dfs(0)

# Read input from stdin
n = int(input())
tree = [int(x) for x in input().split()]

print(maxPathSum(tree))
