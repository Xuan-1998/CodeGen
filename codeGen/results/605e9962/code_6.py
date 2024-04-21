from collections import defaultdict
from sys import stdin

def dfs(node, parent, graph, colors, dp):
    color = 1 if colors[node] == 'W' else -1
    dp[node][color] = 1  # Initialize with the color of the current node
    total_balanced = 0

    for child in graph[node]:
        if child == parent:
            continue
        total_balanced += dfs(child, node, graph, colors, dp)

        # Combine DP states of child into parent
        new_dp = defaultdict(int)
        for c_diff, c_count in dp[node].items():
            for child_diff, child_count in dp[child].items():
                new_dp[c_diff + child_diff] += c_count * child_count
        dp[node] = new_dp

    total_balanced += dp[node][0]  # Balanced subtree rooted at this node
    return total_balanced

def solve():
    n = int(stdin.readline().strip())
    parents = list(map(int, stdin.readline().split()))
    colors = [''] + list(stdin.readline().strip())  # 1-indexed
    graph = defaultdict(list)
    dp = [defaultdict(int) for _ in range(n + 1)]

    # Build the tree graph
    for i in range(2, n + 1):
        graph[parents[i - 2]].append(i)
        graph[i].append(parents[i - 2])

    result = dfs(1, -1, graph, colors, dp)
    print(result)

# Read the number of test cases
t = int(stdin.readline().strip())
for _ in range(t):
    solve()
