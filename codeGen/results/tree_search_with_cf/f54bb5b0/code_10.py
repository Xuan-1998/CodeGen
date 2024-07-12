python
import sys
input = sys.stdin.read
from collections import defaultdict

def solve():
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
    
    # Build the tree
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    # dp[u][d] will store number of paths of length d ending at u
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    def dfs(u):
        visited[u] = True
        dp[u][0] = 1
        for v in tree[u]:
            if not visited[v]:
                dfs(v)
                for d in range(1, k + 1):
                    dp[u][d] += dp[v][d - 1]
    
    def count_pairs(u):
        visited[u] = True
        count = 0
        for v in tree[u]:
            if not visited[v]:
                count += count_pairs(v)
                for d in range(1, k):
                    count += dp[u][d] * dp[v][k - d - 1]
        return count
    
    dfs(1)
    visited = [False] * (n + 1)
    result = count_pairs(1)
    
    print(result)


