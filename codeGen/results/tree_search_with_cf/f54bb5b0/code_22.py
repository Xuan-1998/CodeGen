python
import sys
from collections import defaultdict, deque

def solve():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    k = int(data[1])
    
    if k == 0:
        print(0)
        return
    
    edges = []
    index = 2
    for _ in range(n - 1):
        a = int(data[index])
        b = int(data[index + 1])
        edges.append((a, b))
        index += 2
    
    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    result = [0]
    
    def dfs(node, parent):
        dp[node][0] = 1
        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            dfs(neighbor, node)
            for d in range(1, k + 1):
                dp[node][d] += dp[neighbor][d - 1]
        
        # Count pairs (u, v) such that distance(u, v) = k
        total = 0
        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            for d in range(1, k):
                total += dp[neighbor][d - 1] * (dp[node][k - d] - dp[neighbor][k - d - 1])
        
        result[0] += total // 2
    
    dfs(1, -1)
    
    print(result[0])


