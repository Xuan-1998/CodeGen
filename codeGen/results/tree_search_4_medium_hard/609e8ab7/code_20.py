===BEGIN CODE===
def dfs(node, dp):
    # Base case: leaf node with no children
    if not tree[node]:
        return abs(ranges[node] - lefts[node])

    # Initialize minimum operations for current node
    min_ops = float('inf')

    # Traverse ancestors and calculate minimum operations
    for parent in tree:
        if parent != node and dp[parent] + (ranges[node] - lefts[node]) < min_ops:
            min_ops = dp[parent] + (ranges[node] - lefts[node])

    return min_ops

# Initialize variables for memoization
dp = [0] * n
tree = [[] for _ in range(n)]

# Read input from stdin and populate tree data structure
n, = map(int, stdin.readline().split())
for i in range(1, n):
    p, = map(int, stdin.readline().split())
    tree[p].append(i)

# Populate ranges and lefts arrays
for i in range(n):
    l, r, = map(int, stdin.readline().split())
    ranges[i], lefts[i] = r, l

# Perform DFS traversal with memoization to calculate minimum operations
for i in range(1, n):
    dp[i] = dfs(i, dp)

# Print the minimum number of operations needed for each subtree
for min_ops in dp[1:]:
    print(min_ops)
