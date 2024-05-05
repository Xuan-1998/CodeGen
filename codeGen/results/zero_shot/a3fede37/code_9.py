def max_path_sum(tree):
    def dfs(i):
        if i < 0 or i >= len(tree):
            return 0
        left = dfs(2 * i + 1)
        right = dfs(2 * i + 2)
        return tree[i] + max(left, right)

    return max(dfs(0), key=abs)

# Read input from stdin
tree = [int(x) for x in input().split()]

# Calculate the maximum sum of a path
max_sum = max_path_sum(tree)

# Print the answer to stdout
print(max_sum)
