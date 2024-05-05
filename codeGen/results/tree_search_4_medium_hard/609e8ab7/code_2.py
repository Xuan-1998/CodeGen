def dp(node, memo):
    if node not in memo:
        memo[node] = 0

        # Calculate the minimum number of operations required to adjust all vertices at node node
        # Consider the adjustment required for the current node itself (within its range)
        # and the adjustments required for its children (recursively computed using memo[child] values)

        # Iterate over each child node
        for child in range(1, node + 1):
            if parent[child] == node:
                # If the child is an ancestor of the current node, consider adjusting by adding a value
                memo[node] += min(r_child - l_child + dp(child, memo) for r_child in range(l_child, r_child + 1))
        memo[node] = min(memo[node], dp(node, memo))

    return memo[node]

# Read input from stdin
n = int(input())
parent = [int(input()) for _ in range(n - 1)]
ranges = [[int(input()), int(input())] for _ in range(n)]

memo = {}
min_operations = []
for node in range(1, n + 1):
    min_operations.append(dp(node, memo))

# Print the answer to stdout
print('\n'.join(map(str, min_operations)))
