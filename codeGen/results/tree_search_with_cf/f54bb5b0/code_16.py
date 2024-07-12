python
import sys
input = sys.stdin.read
sys.setrecursionlimit(100000)

def solve():
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    
    from collections import defaultdict
    
    # Create adjacency list for the tree
    graph = defaultdict(list)
    index = 2
    for _ in range(n - 1):
        a = int(data[index]) - 1
        b = int(data[index + 1]) - 1
        graph[a].append(b)
        graph[b].append(a)
        index += 2

    # dp[u][d] will store the number of vertices at distance d from vertex u
    dp = [[0] * (k + 1) for _ in range(n)]
    
    # To store the final result
    result = [0]

    def dfs(u, parent):
        dp[u][0] = 1  # Distance to itself is 0
        
        for v in graph[u]:
            if v == parent:
                continue
            dfs(v, u)
            
            # Combine results from child v to parent u
            for d in range(1, k + 1):
                result[0] += dp[u][d - 1] * dp[v][k - d]
            
            # Update dp[u] using dp[v]
            for d in range(1, k + 1):
                dp[u][d] += dp[v][d - 1]

    # Start DFS from vertex 0 (assuming 0-based indexing)
    dfs(0, -1)
    
    # Print the result
    print(result[0])

if __name__ == "__main__":
    solve()

