import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000)

def count_pairs(n, k, edges):
    # Initialize the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Initialize dp table
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = 1
    
    # DFS function to fill dp table
    def dfs(node, parent):
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            dfs(neighbor, node)
            for d in range(1, k + 1):
                dp[node][d] += dp[neighbor][d - 1]
    
    # Perform DFS from node 1 (assuming 1 is always a valid node)
    dfs(1, -1)
    
    # Count the number of valid pairs
    result = 0
    for node in range(1, n + 1):
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            for d in range(1, k):
                result += dp[node][d] * dp[neighbor][k - d - 1]
    
    # Add the pairs that don't go through a common parent
    for node in range(1, n + 1):
        result += dp[node][k]
    
    # Each pair is counted twice, so divide by 2
    return result // 2

if __name__ == "__main__":
    # Read input
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    edges = []
    index = 2
    for i in range(n - 1):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        index += 2
    
    # Calculate and print the result
    result = count_pairs(n, k, edges)
    print(result)

