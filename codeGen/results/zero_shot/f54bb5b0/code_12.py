python
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000)

def dfs(node, parent, adj, dp, k):
    dp[node][0] = 1
    count = 0

    for neighbor in adj[node]:
        if neighbor == parent:
            continue
        count += dfs(neighbor, node, adj, dp, k)
        for d in range(1, k + 1):
            count += dp[node][d - 1] * dp[neighbor][k - d]
        for d in range(1, k + 1):
            dp[node][d] += dp[neighbor][d - 1]

    return count

def count_pairs(n, k, edges):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    result = dfs(1, -1, adj, dp, k)
    return result

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    k = int(data[1])
    edges = []
    index = 2
    for _ in range(n - 1):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        index += 2

    result = count_pairs(n, k, edges)
    print(result)

