import sys
input = sys.stdin.read
from collections import defaultdict, deque

def solve():
    data = input().strip().split()
    n = int(data[0])
    k = int(data[1])
    
    if k > n - 1:
        print(0)
        return
    
    edges = data[2:]
    adj = defaultdict(list)
    
    for i in range(n - 1):
        a = int(edges[2 * i])
        b = int(edges[2 * i + 1])
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
                result[0] += dp[node][d - 1] * dp[neighbor][k - d]
            for d in range(1, k + 1):
                dp[node][d] += dp[neighbor][d - 1]
    
    dfs(1, -1)
    print(result[0])

if __name__ == "__main__":
    solve()

