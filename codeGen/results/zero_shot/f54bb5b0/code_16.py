python
import sys
from collections import defaultdict, deque

input = sys.stdin.read
sys.setrecursionlimit(100000)

def count_pairs(n, k, edges):
    # Build the tree using adjacency list
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    # Initialize the DP array
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    result = [0] * (n + 1)
    
    def dfs(node, parent):
        dp[node][0] = 1
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            dfs(neighbor, node)
            for i in range(k):
                result[node] += dp[node][i] * dp[neighbor][k - i - 1]
            for i in range(k):
                dp[node][i + 1] += dp[neighbor][i]
    
    dfs(1, -1)
    
    return sum(result) // 2

if __name__ == "__main__":
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    edges = []
    for i in range(n - 1):
        a = int(data[2 + 2 * i])
        b = int(data[3 + 2 * i])
        edges.append((a, b))
    
    print(count_pairs(n, k, edges))

