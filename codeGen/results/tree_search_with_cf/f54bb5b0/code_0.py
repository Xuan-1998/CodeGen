import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000)

def dfs(u, parent, k, adj, dp, count):
    dp[u][0] = 1  # The distance from u to itself is 0
    for v in adj[u]:
        if v == parent:
            continue
        dfs(v, u, k, adj, dp, count)
        # Count pairs with distance exactly k
        for d in range(1, k):
            count[0] += dp[u][d-1] * dp[v][k-d-1]
        
        # Update dp[u] with values from dp[v]
        for d in range(1, k+1):
            dp[u][d] += dp[v][d-1]

def main():
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
    
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    count = [0]
    
    dfs(1, -1, k, adj, dp, count)
    
    print(count[0])

if __name__ == "__main__":
    main()

