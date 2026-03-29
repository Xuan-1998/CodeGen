import sys
input = sys.stdin.read
from collections import defaultdict, deque

def solve():
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    
    if k == 0:
        print(0)
        return
    
    adj = defaultdict(list)
    index = 2
    for _ in range(n - 1):
        a = int(data[index])
        b = int(data[index + 1])
        adj[a].append(b)
        adj[b].append(a)
        index += 2
    
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
        
        # Count pairs with paths of length exactly k passing through `node`
        total_paths_through_node = 0
        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            for d in range(1, k):
                total_paths_through_node += dp[neighbor][d - 1] * (dp[node][k - d] - dp[neighbor][k - d - 1])
        
        result[0] += total_paths_through_node // 2
    
    dfs(1, -1)
    
    print(result[0])

solve()

