import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000)

def solve():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    k = int(data[1])
    
    adj = defaultdict(list)
    index = 2
    for _ in range(n - 1):
        a = int(data[index])
        b = int(data[index + 1])
        adj[a].append(b)
        adj[b].append(a)
        index += 2
    
    # Initialize the DP table
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = 1
    
    def dfs(node, parent):
        nonlocal result
        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            dfs(neighbor, node)
            # Update dp table for the current node
            for d in range(1, k + 1):
                dp[node][d] += dp[neighbor][d - 1]
        
        # Count pairs
        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            for d in range(k):
                result += dp[node][d] * dp[neighbor][k - d - 1]
    
    result = 0
    dfs(1, -1)
    
    print(result)


