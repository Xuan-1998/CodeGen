import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000)

def read_input():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    edges = []
    index = 2
    for _ in range(n - 1):
        a = int(data[index])
        b = int(data[index + 1])
        edges.append((a, b))
        index += 2
    return n, k, edges

def dfs(node, parent, adj, dp, k):
    dp[node][0] = 1  # Distance 0 to itself
    for neighbor in adj[node]:
        if neighbor == parent:
            continue
        dfs(neighbor, node, adj, dp, k)
        for d in range(k):
            dp[node][d + 1] += dp[neighbor][d]

def count_pairs(node, parent, adj, dp, k):
    count = 0
    for neighbor in adj[node]:
        if neighbor == parent:
            continue
        
        # Count pairs where one node is in the subtree of `neighbor` and the other node is in the subtree of `node`
        for d in range(k):
            count += dp[neighbor][d] * dp[node][k - d - 1]
        
        count += count_pairs(neighbor, node, adj, dp, k)
    
    return count

def main():
    n, k, edges = read_input()
    
    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Start DFS from node 1 (assuming node indices are 1-based)
    dfs(1, -1, adj, dp, k)
    
    # Count pairs
    result = count_pairs(1, -1, adj, dp, k)
    
    print(result)

if __name__ == "__main__":
    main()

