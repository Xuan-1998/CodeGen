import sys
input = sys.stdin.read
sys.setrecursionlimit(100000)

def solve():
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    
    edges = []
    index = 2
    for _ in range(n - 1):
        a, b = int(data[index]), int(data[index + 1])
        edges.append((a, b))
        index += 2
    
    # Build the adjacency list
    adj = [[] for _ in range(n + 1)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    
    # dp[u][d] will store the number of vertices at distance d from vertex u
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    def dfs(u, parent):
        dp[u][0] = 1
        for v in adj[u]:
            if v == parent:
                continue
            dfs(v, u)
            for d in range(k):
                dp[u][d + 1] += dp[v][d]
    
    def count_pairs():
        count = 0
        def dfs_count(u, parent):
            nonlocal count
            for v in adj[u]:
                if v == parent:
                    continue
                dfs_count(v, u)
                # Count pairs (u, w) where the path length is exactly k
                for d1 in range(k):
                    d2 = k - d1 - 1
                    if d2 >= 0:
                        count += dp[u][d1] * dp[v][d2]
            # Combine the dp values of the children into the current node
            for v in adj[u]:
                if v == parent:
                    continue
                for d in range(k):
                    dp[u][d + 1] += dp[v][d]
        
        dfs_count(1, -1)
        return count
    
    # Run DFS to populate the dp table
    dfs(1, -1)
    # Calculate the number of pairs with path length exactly k
    result = count_pairs()
    
    # Output the result
    print(result)

if __name__ == "__main__":
    solve()

