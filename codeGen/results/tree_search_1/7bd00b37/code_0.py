MOD = 998244353

def dfs(node, parent, graph, subtree_size, dp):
    subtree_size[node] = 1
    dp[node] = 1
    for child in graph[node]:
        if child != parent:
            dfs(child, node, graph, subtree_size, dp)
            # Calculate the number of ways to arrange the children of a node in a circle
            dp[node] = dp[node] * dp[child] * subtree_size[node] % MOD
            # Update the size of the subtree
            subtree_size[node] += subtree_size[child]

def solve(n, edges):
    graph = [[] for _ in range(n + 1)]
    subtree_size = [0] * (n + 1)
    dp = [0] * (n + 1)
    
    # Build the graph
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Perform DFS and DP
    dfs(1, -1, graph, subtree_size, dp)
    
    # The answer is the DP value at the root node
    return dp[1]

# Read input from stdin
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Solve the problem and output the answer
print(solve(n, edges))
