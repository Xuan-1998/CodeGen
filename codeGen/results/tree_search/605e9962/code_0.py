from collections import defaultdict
from sys import stdin, stdout

def dfs(node, parent, tree, colors, dp):
    color = 1 if colors[node] == 'W' else -1
    dp[node] = defaultdict(int)
    dp[node][color] = 1
    balanced_subtrees = 0

    for child in tree[node]:
        if child != parent:
            balanced_subtrees += dfs(child, node, tree, colors, dp)

            # Combine the DP states from child into the current node
            new_dp = defaultdict(int)
            for diff in dp[node]:
                for child_diff in dp[child]:
                    new_dp[diff + child_diff] += dp[node][diff] * dp[child][child_diff]

            dp[node] = new_dp

    # Count the balanced subtrees that include the current node
    balanced_subtrees += dp[node][0]
    return balanced_subtrees

def count_balanced_subtrees(tree, colors):
    n = len(tree)
    dp = [None] * n
    return dfs(0, -1, tree, colors, dp)

# Read the number of test cases
t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    parents = list(map(int, stdin.readline().split()))
    colors = stdin.readline().strip()

    # Construct the tree
    tree = [[] for _ in range(n)]
    for i in range(1, n):
        tree[parents[i - 1] - 1].append(i)

    result = count_balanced_subtrees(tree, colors)
    stdout.write(str(result) + '\n')
