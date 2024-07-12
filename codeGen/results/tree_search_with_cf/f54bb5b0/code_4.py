python
import sys
input = sys.stdin.read
from collections import defaultdict, deque

def count_pairs(n, k, edges):
    # Initialize the graph
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # Initialize dp array
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Global counter for valid pairs
    result = 0
    
    def dfs(u, parent):
        nonlocal result
        dp[u][0] = 1  # Base case: distance 0 from itself
        
        for v in graph[u]:
            if v == parent:
                continue
            dfs(v, u)
            # Count pairs with distance k
            for d in range(1, k + 1):
                result += dp[u][d - 1] * dp[v][k - d]
            # Combine dp values of child v into dp values of u
            for d in range(1, k + 1):
                dp[u][d] += dp[v][d - 1]
    
    # Start DFS from vertex 1 (assuming 1 as the root)
    dfs(1, -1)
    
    return result

def main():
    data = input().strip().split()
    n = int(data[0])
    k = int(data[1])
    edges = [(int(data[i]), int(data[i + 1])) for i in range(2, len(data), 2)]
    
    result = count_pairs(n, k, edges)
    print(result)

if __name__ == "__main__":
    main()

